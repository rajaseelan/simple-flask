from flask import Flask
import os
import platform
import time
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return json_response()

def json_response():
    response = {
        "hostname": hostname(),
        "time": current_time()
    }

    return json.dumps(response, sort_keys=True, indent=4)


def hostname():
    name = os.getenv('SIMPLE_FLASK_HOSTNAME')
    if name == None:
        name = platform.node()
    
    if name == "":
        name = "no-hostname"
    
    return name

def current_time():
    return str(time.time())