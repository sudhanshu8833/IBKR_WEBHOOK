from flask import Flask, jsonify,request
import json
import traceback
import subprocess
from ib_insync import *

import time
import os
app = Flask(__name__)


def place_order(data):

    try:
        args_json = json.dumps(data)
        # Command to run example_program.py with arguments
        print(os.path.join(os.path.dirname(os.path.abspath(__file__)), "env/bin/python3"), os.path.join(os.path.dirname(os.path.abspath(__file__)), "run.py"))
        command = [os.path.join(os.path.dirname(os.path.abspath(__file__)), "env/bin/python3"), os.path.join(os.path.dirname(os.path.abspath(__file__)), "run.py"), args_json]
        subprocess.run(command)
        # Run the command
        # command=['pip3','freeze']
        # print(subprocess.run(command))
        # subprocess.run(command)

    except Exception:
        return str(traceback.format_exc())


@app.route('/')
def hello():
    # while True:
    #     time.sleep(1)
    print("BHAGWAN KIS GANAM DE RHAI HO?")
    return "Hello, World!"
        

@app.route('/ad/tradingview_webhook/', methods=['POST'])
def post_data():
    # Check if the request contains JSON data
    try:
        if request.method=="POST":
            # Retrieve the JSON data from the request
            data = request.get_json()
            passphrase=data['passphrase']
            pp = str(passphrase)
            data['Order_id']=[]

            if pp== "dfkhskhfiuaehg":
                id=0
                id=place_order(data)
                data['Order_id'].append(id)

                return jsonify(data)

            else:
                return jsonify({"error":"passphrase is wrong"})

        return jsonify({"error":"send a valid post request"})
    
    except Exception:
        return jsonify({"error":str(traceback.format_exc())})

if __name__ == '__main__':
    app.run(port=4050)
