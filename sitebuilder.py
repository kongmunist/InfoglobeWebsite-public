from flask import Flask, render_template, request, jsonify, url_for, redirect, send_from_directory
# from flask_flatpages import FlatPages
# from flask_frozen import Freezer
import os, sys
import json
from datetime import datetime

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# app.config['DEBUG'] = True
MSG_LIMIT = 3
MAX_LENGTH = 38
# freezer = Freezer(app)

@app.route('/main', methods = ['POST', 'GET'])
def main():
    return render_template("main.html")

# TODO:
# no repeats
# no empty
# delete button per message
# fun infoglobe visualizer that spins


@app.route('/savemessage', methods = ['POST'])
def save_msg():
    data = []
    if request.method == 'POST':
        try:
            with open('static/messages.txt', 'r') as f:
                data = f.read().strip().split('\n')
        except:
            pass

        with open('static/messages.txt', 'w') as f:
            msg = request.get_json()
            msg = msg[:MAX_LENGTH]
            if (msg not in data):
                data.insert(0, msg)

            data = data[:3]
            f.write("\n".join(data))

        with open('static/messages.json', "w+") as f:
            d = dict()
            for i,msg in enumerate(data):
                d["msg" + str(i)] = msg
            f.write(json.dumps(d))


        # Add to permanent log:
        # datetime object containing current date and time + message
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with open('static/log.txt', "a") as f:
            f.write(dt_string + ": " + request.get_json() + "\n")

    return jsonify(data)



@app.route('/', methods = ['GET'])
def index():
    data = []
    if (request.method == "GET"):
        try:
            with open('static/messages.txt', 'r') as f:
                data = f.read().strip().split('\n')
        except:
            pass
    return render_template("form.html", values=data)


# We need it now, going to /json delivers the .json file
@app.route('/json')
def jsonFile():
    # d['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('static/messages.json', "r+") as f:
        d = json.loads(f.read())
        d.update({"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        f.seek(0)
        f.write(json.dumps(d))

    # return redirect(url_for('static', filename='messages.json'))
    return send_from_directory("static", 'messages.json')

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response



if __name__ == "__main__":
    app.run(port=8000, debug=True)
