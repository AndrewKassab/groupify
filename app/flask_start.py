import os
import json
import datetime
from flask import Flask
app = Flask(__name__)

# See:
# http://flask.pocoo.org/docs/1.0/quickstart
# for more info on using Flask

@app.route('/')
def hello_world():
    return 'Hello, World!'
