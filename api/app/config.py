# Flask Settings
bind_address = '0.0.0.0'
port = 8080
debug = True

# Swagger Settings
swagger_doc_url = '/apidoc'

# Connect with FHIR?
use_fhir = False
fhir_url = "http://fhir:8080/baseDstu3"

# Datastore / Forms
template_dir = "/data/forms/"
output_dir = "/usr/src/app/static"