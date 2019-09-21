from flask import Flask
from flask_cors import CORS

import config
from endpoints import api

# trollface.jpg
from textmagic.rest import TextmagicRestClient


# See
# http://flask.pocoo.org/snippets/35/

class ReverseProxied(object):
    '''Wrap the application in this middleware and configure the
    front-end server to add these headers, to let you quietly bind
    this to a URL other than / and to an HTTP scheme that is
    different than what is used locally.

    In nginx:
    location /myprefix {
        proxy_pass http://192.168.0.1:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Scheme $scheme;
        proxy_set_header X-Script-Name /myprefix;
        }

    :param app: the WSGI application
    '''
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
        if script_name:
            environ['SCRIPT_NAME'] = script_name
            path_info = environ['PATH_INFO']
            if path_info.startswith(script_name):
                environ['PATH_INFO'] = path_info[len(script_name):]

        scheme = environ.get('HTTP_X_SCHEME', '')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)

app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)
CORS(app)

def configure(flask_app):
    pass

def initialise(flask_app):
    configure(flask_app)
    api.init_app(app)

if __name__ == "__main__":


    #username = "aqeelakber"
    #token = "VJ6O0aVQqaz5i6w3oNt7MWVgTnHnvy"
    #client = TextmagicRestClient(username, token)
    #message = client.messages.create(phones="+61430204771", text="Hello TextMagic")

    initialise(app)
    app.run(
        host=config.bind_address, \
        port=config.port, \
        debug=config.debug
    )
