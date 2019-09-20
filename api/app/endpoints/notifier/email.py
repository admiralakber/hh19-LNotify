# Flask API Libraries
from flask_restplus import Namespace, Resource, fields, reqparse

from endpoints.lnotify import api

@api.route('/email')
class Email(Resource):
    @api.doc("Send an Email Notification to the Patient")
    #@api.marshal_list_with(patient)
    def post(self):
        return