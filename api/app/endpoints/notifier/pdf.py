# Flask API Libraries
from flask_restplus import Namespace, Resource, fields, reqparse

from endpoints.lnotify import api

@api.route('/pdf')
class PDF(Resource):
    @api.doc("Given a Patient ID return the Full Details")
    #@api.marshal_list_with(patient)
    def post(self):
        return