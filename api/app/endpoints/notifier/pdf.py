# Flask API Libraries
from flask_restplus import Namespace, Resource, fields, reqparse

# drawing tools
import pdfrw

# stdlib
import os
import hashlib

# lnotify
from endpoints.lnotify import api

# project
import config

# Thanks
# https://bostata.com/how-to-populate-fillable-pdfs-with-python/

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)


# Thanks past Aqeel =) 
# https://github.com/pmRed/govhack2018-EZ1/blob/master/blockchain/api/main.py
hashfunclong = lambda x: hashlib.sha1(x.encode("UTF-8")).hexdigest()


@api.route('/pdf')
class PDF(Resource):
    @api.doc("Given appointment details, make a PDF")
    #@api.marshal_list_with(patient)
    def get(self):
        fillpdf = {
            "Name" : "David Yohan",
            "AppointmentWith" : "Dr Doctor Who",
            "Phone" : "+61430204771",
            "Address" : "The place over there",
            "Date" : "2019-09-21",
            "Time" : "11:00 AM",
            "Interpreter" : "Yes"
        }

        appointment_hash = hashfunclong("|".join(fillpdf.values()))

        write_fillable_pdf("{}/pdfs/{}/{}.pdf".format(config.template_dir, "Arabic", "Arabic"), 
                        "{}/{}.pdf".format(config.output_dir, appointment_hash), fillpdf)

        return {"appointment_id" : appointment_hash}
    