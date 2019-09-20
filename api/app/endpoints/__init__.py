from flask_restplus import Api

from endpoints.fhir import api as fhir
from endpoints.lnotify import api as lnotify

import config

api = Api(
    title='HealthHack2019: Multilingual Appointment Notifier',
    version='1.0',
    description='API to Multilingual Appointment Notifier',
    doc=config.swagger_doc_url
)

api.add_namespace(fhir)
api.add_namespace(lnotify)
