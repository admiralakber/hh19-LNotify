# Flask API Libraries
from flask_restplus import Namespace, Resource, fields, reqparse

from endpoints.lnotify import api

# stdlib
import urllib.parse
import json

# trollface.jpg
from textmagic.rest import TextmagicRestClient

def sms(fillsms : dict) -> dict:

    # TextMagic 
    username = "aqeelakber"
    token = "VJ6O0aVQqaz5i6w3oNt7MWVgTnHnvy"
    client = TextmagicRestClient(username, token)

    # generate maps url
    address = "+".join(fillsms["Address"].split(" "))
    address = urllib.parse.quote(address)
    maps_url = "https://www.google.com/maps/dir/?api=1&destination={}&travelmode=transit".format(address)

    phones = ["+61430204771"]
    text = "Hello from Culture Fluent... \nDIRECTIONS VIA MAPS: {}".format(maps_url)

    try:
        #message = client.messages.create(phones=",".join(phones), text=text)
        return {"sms" : phones, "text" : text}
    except:
        return {"sms" : phones, "text" : text, "failed" : True}
