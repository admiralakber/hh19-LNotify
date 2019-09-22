# Flask API Libraries
from flask_restplus import Namespace, Resource, fields, reqparse
from flask import render_template, make_response, redirect, url_for

import numpy as np

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

    # hard coded hack
    phones = [fillsms["Mobile"], ]

    memes = []
    if True:
        numbers = np.loadtxt("/data/forms/numbers.csv", dtype=str)
        for n in numbers:
            memes.append(n)
        print(memes, flush=True)

    text = []
    text.append("Hello {}.".format(fillsms["Name"]))
    text.append("Your Health Appointment is booked with {} at {} {}.".format(fillsms["AppointmentWith"], fillsms["Date"], fillsms["Time"]))
    text.append("Phone: {}.".format(fillsms["Phone"]))
    
    # if audio...
    audio = None
    translate_code = "en" # 
    if fillsms['Audio']:
        # get the stuff before the url
        read = "\n".join(text)
        lang = fillsms['Language'].capitalize()
        print("Trying to find Audio for Language = {}".format(lang), flush=True)
        translator = Translator()
        for key,short in reversed_ttslangs.items():
            if lang in key:
                translation = translator.translate(read, dest=short)
                audio = gtts.gTTS(translation.text, lang=short)
                translate_code = short
                print("AUDIO LANGUAGE: {}".format(short), flush=True)
        if audio:
            audiotext = translator.translate("AUDIO", dest=translate_code).text
            audio.save("{}/{}.mp3".format(config.output_dir, appointment_hash))
            text.append("{}: {}.".format(audiotext, "https://api.culturefluent.thaum.io/LNotify/audio/"+appointment_hash))

    maptext = translator.translate("DIRECTIONS", dest=translate_code).text
    text.append("DIRECTIONS: {}".format(maptext,maps_url))

    print("Text", text, flush=True)
    print("slice", " ".join(text[:-2]), flush=True)
    print("other", " ".join(text[-2:]), flush=True)
    translation =  translator.translate(" ".join(text[:-2]), dest=translate_code)
    trans_text = translation.text + "\n\n" + "\n\n".join(text[-2:])

    
    try:
        message = client.messages.create(phones=",".join(phones), text=trans_text)
        return {"sms" : phones, "text" : text, "appointment_id" : appointment_hash}
    except:
        message = client.messages.create(phones=",".join(phones), text=" ".join(text[:-2]) + "\n\n" + "\n\n".join(text[-2:]))
        return {"sms" : phones, "text" : text, "sms_failed" : True, "appointment_id" : appointment_hash}

@api.route("/audio/<string:appointment_id>")
class HTMLRender(Resource):
    def get(self, appointment_id):
        headers = {'Content-Type': 'text/html'}
        html = render_template("audio.html", appointment_id=appointment_id)
        return make_response(html, 200, headers)
