# Flask API Libraries
from flask_restplus import Namespace, Resource, fields, reqparse

# FHIR HL7 Database Client
# https://github.com/smart-on-fhir/client-py
import fhirclient.client
import fhirclient.models.patient

# stdlib
import time
from collections import OrderedDict

# Project Config
import config

# Import dummy data
import endpoints.data

#
# BEGIN HERE
#

## Connect to the FHIR Database
if config.use_fhir:
    smart = fhirclient.client.FHIRClient({'app_id' : 'lnotify', 'api_base' : config.fhir_url})
    search = fhirclient.models.patient.Patient.where(struct={"language:not" : "en-US"})
    patients = search.perform_resources(smart.server)
    for p in patients:
        print(p.as_json()["communication"], flush=True)

## Print Dummy Data
for p in endpoints.data.patients.values():
    print(p, flush=True)

## Start setting up the API
api = Namespace("FHIR", description="FHIR Querier")

# Compliant with FHIR 4.0 HL7 Standard
# https://www.hl7.org/fhir/patient.html

communication = api.model("Communication", {
    "language" : fields.String("Language Code, the language which can be used to communicate with the patient about their health"),
    "preferred" : fields.Boolean("Language preference indicator")
})

contactpoint = api.model("ContactPoint", {
    "system" : fields.String(description="code"),
    "value" : fields.String(description="The actual contact point details")
})

patient = api.model("Patient", {
    "id" : fields.String(description="Patient Resource ID"),
    "name" : fields.String(description="Human Name, A name associated with the patient"),
    "telecom" : fields.List(fields.Nested(contactpoint)),
    "communication" : fields.List(fields.Nested(communication)),
    "generalPractitioner" : fields.String(description="Patient's nominated primary care provider"),
    "managingOrganization" : fields.String(description="Organization that is the custodian of the patient record")
})

# Compliant with FHIR 4.0 HL7 Standard
# https://www.hl7.org/fhir/practitioner.html
practioner = api.model("Practitioner", {
    "name" : fields.String("Human Name, the name(s) associated with the practitioner")
})

reqpar_patient = reqparse.RequestParser()
reqpar_patient.add_argument('id', 
    type=str, 
    help="Identifier Associated with the Patient",
    required=True)

@api.route('/patient/details')
@api.expect(reqpar_patient)
class Patient(Resource):
    @api.doc("Given a Patient ID return the Full Details")
    @api.marshal_list_with(patient)
    def post(self):
        args = reqpar_patient.parse_args()['id']
        return endpoints.data.patients[args]

@api.route("/patients")
class Patients(Resource):
    @api.doc("List of Patients and Names")
    def get(self):
        resp = []
        for i, details in endpoints.data.patients.items():
            r = {"key" : i, "text" : details["name"], "value" : i}
            resp.append(r)
        return resp

@api.route("/doctors")
class Doctors(Resource):
    @api.doc("List of Doctors and Names")
    def get(self):
        print("doctors", flush=True)
        resp = []
        for i, details in enumerate(endpoints.data.doctors):
            r = {"key" : i, "text" : details[0], "value" : details[1]}
            resp.append(r)
        return resp

@api.route("/languages")
class Languages(Resource):
    @api.doc("List of all the languages")
    def get(self):
        langs = []
        # loop and search
        for i, details in endpoints.data.patients.items():
            r = {"key" : i, "text" : details["name"], "value" : i}
            # collect all
            for l in details["communication"]:
                langs.append(l["language"])
        # deduplicate
        langs = list(set(langs))
        # format response
        resp = []
        for i, l in enumerate(langs):
            r = {"key" : i, "text" : l.capitalize(), "value" : l.lower()}
            resp.append(r)
        return resp
