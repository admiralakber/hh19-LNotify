# Flask API Libraries
from flask_restplus import Namespace, Resource, fields, reqparse, cors


# stdlib
import time
from collections import OrderedDict
from datetime import datetime

# Project Config
import config
import endpoints.data


#
# BEGIN HERE
#

# Set up namespace
api = Namespace("LNotify", description="Multilingual Appointment Notifier")

from endpoints.notifier.pdf import *
from endpoints.notifier.sms import *
from endpoints.notifier.email import *

reqpar = reqparse.RequestParser()
reqpar.add_argument('dateTime', 
    type=str, 
    help="Date and Time",
    required=False)
reqpar.add_argument('doctor', 
    type=int, 
    help="Doctor ID",
    required=False)
reqpar.add_argument('interp', 
    type=bool, 
    help="Interpreter Organised?",
    required=False)
reqpar.add_argument('language', 
    type=str, 
    help="Language",
    required=False)
reqpar.add_argument('name', 
    type=str, 
    help="Notification Name",
    required=False)
reqpar.add_argument('patient', 
    type=str, 
    help="Patient ID",
    required=False)
reqpar.add_argument('vision', 
    type=bool, 
    help="Vision impair, auto accessible",
    required=False)

@api.route('/notify')
@api.expect(reqpar)
class Notifier(Resource):
    @api.doc("Creates the correct notification and returns")
    @cors.crossdomain(origin='*')
    def get(self):
        args = reqpar.parse_args()
        Name = endpoints.data.patients[args['patient']]['name']
        #DateTime = arrow.get(args['dateTime'])
        DateTime = datetime.strptime(args['dateTime'], "%d-%m-%Y %H:%M")
        Date = DateTime.strftime("%A %d %B %Y")
        Time = DateTime.strftime("%I:%M %p")
        AppointmentWith = endpoints.data.doctors[args['doctor']][0]
        Interpreter = str(args['interp'])
        Address = endpoints.data.doctors[args['doctor']][1]
        Language = args['language']
        VisionImpaired = str(args['vision'])
        
        NotificationType = args['name']

        if NotificationType == "print":
            fillpdf = {
                "Name" : Name,
                "AppointmentWith" : AppointmentWith,
                "Phone" : "3811 1232",
                "Address" : Address,
                "Date" : Date,
                "Time" : Time,
                "Interpreter" : Interpreter,
                "Language" : Language
            }
            
            return pdf(fillpdf)

