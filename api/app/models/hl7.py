""" API Model for HL7 Patient
"""

from flask_restplus import Namespace, fields

api = Namespace("lnotify", description="Multilingual Appointment Notifier")

# Compliant with FHIR 4.0 HL7 Standard
# https://www.hl7.org/fhir/patient.html

communication = api.model("Communication", {
    "language" : fields.String("Language Code, the language which can be used to communicate with the patient about their health"),
    "preferred" : fields.Boolean("Language preference indicator")
})

patient = api.model("Patient", {
    "name" : fields.String(description="Human Name, A name associated with the patient"),
    "telecom" : fields.Integer(description="Contact Point, a contact detail for the individual"),
    "communication" : fields.List(fields.Nested(communication)),
    "generalPractitioner" : fields.String(description="Patient's nominated primary care provider"),
    "managingOrganization" : fields.String(description="Organization that is the custodian of the patient record")
})

# Compliant with FHIR 4.0 HL7 Standard
# https://www.hl7.org/fhir/practitioner.html
practioner = api.model("Practitioner", {
    "name" : fields.String("Human Name, the name(s) associated with the practitioner")
})