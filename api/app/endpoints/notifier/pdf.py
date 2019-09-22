# Flask API Libraries
from flask_restplus import Namespace, Resource, fields, reqparse
from flask import render_template, make_response, redirect, url_for


# drawing tools
import pdfrw
from pdf2image import convert_from_path

# stdlib
import os
import hashlib
import subprocess

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

# Do the thing in a function so we can call it elsewhere
def pdf(fillpdf : dict) -> dict:
    # generate a hash for this appointment
    appointment_hash = hashfunclong("|".join(fillpdf.values()))

    # fill the pdf and save it in /output/<hash>.pdf
    write_fillable_pdf("{}/pdfs/{}/{}.pdf".format(config.template_dir, fillpdf['Language'].capitalize(), fillpdf['Language'].capitalize()), 
                        "{}/{}.pdf".format(config.output_dir, appointment_hash), fillpdf)

    # HERE COMES THE HACKS
    # turn the pdf into a rasterized picture
    images = convert_from_path("{}/{}.pdf".format(config.output_dir, appointment_hash))
    images[0].save("{}/{}.png".format(config.output_dir, appointment_hash))
    subprocess.call(["convert", 
                    "{}/{}.png".format(config.output_dir, appointment_hash),
                    "-bordercolor", "white",
                    "-border", "10",
                    "-fuzz", "75%",
                    "-trim", "+repage",
                    "{}/{}_crop.png".format(config.output_dir, appointment_hash)])

    return {"appointment_id" : appointment_hash, "url" : "https://api.culturefluent.thaum.io/LNotify/card/{}".format(appointment_hash)}
    #return redirect('http://localhost:8081/card/{}'.format(appointment_hash))

@api.route("/card/<string:appointment_id>")
class HTMLRender(Resource):
    def get(self, appointment_id):
        headers = {'Content-Type': 'text/html'}
        html = render_template("appointment.html", appointment_id=appointment_id)
        return make_response(html, 200, headers)