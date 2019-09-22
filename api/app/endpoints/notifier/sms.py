# Flask API Libraries
from flask_restplus import Namespace, Resource, fields, reqparse
from flask import render_template, make_response, redirect, url_for



from endpoints.lnotify import api

# stdlib
import urllib.parse
import json
import hashlib

# project
import config

# trollface.jpg
from textmagic.rest import TextmagicRestClient
from googletrans import Translator
import gtts
ttslangs = gtts.lang.tts_langs()
reversed_ttslangs = { v : k for k,v in ttslangs.items() }

# Thanks past Aqeel =) 
# https://github.com/pmRed/govhack2018-EZ1/blob/master/blockchain/api/main.py
hashfunclong = lambda x: hashlib.sha1(x.encode("UTF-8")).hexdigest()


def sms(fillsms : dict) -> dict:
    # appointment hash
    appointment_hash = hashfunclong("|".join(fillsms.values()))

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

    # if audio...
    audio = None
    if fillsms['Audio']:
        # get the stuff before the url
        read = text.split(": https://")[0]
        lang = fillsms['Language']
        print("Trying to find Audio for Language = {}".format(lang), flush=True)
        translator = Translator()
        for key,short in reversed_ttslangs.items():
            if lang in key:
                translation = translator.translate(read, dest=short)
                audio = gtts.gTTS(translation.text, lang=short)
                print("AUDIO LANGUAGE: {}".format(short), flush=True)
        if audio:
            audio.save("{}/{}.mp3".format(config.output_dir, appointment_hash))

    try:
        #message = client.messages.create(phones=",".join(phones), text=text)
        return {"sms" : phones, "text" : text, "appointment_id" : appointment_hash}
    except:
        return {"sms" : phones, "text" : text, "sms_failed" : True, "appointment_id" : appointment_hash}

@api.route("/audio/<string:appointment_id>")
class HTMLRender(Resource):
    def get(self, appointment_id):
        headers = {'Content-Type': 'text/html'}
        html = render_template("audio.html", appointment_id=appointment_id)
        return make_response(html, 200, headers)