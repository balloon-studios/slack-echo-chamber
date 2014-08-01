import json
import requests
from flask import Flask, request, jsonify
from os import environ
from sys import exit


app = Flask(__name__)
endpoint = environ.get('SLACK_WEBHOOK')

@app.route("/", methods=['POST'])
def webhook():
    headers = { 'Content-type': 'application/json' }
    payload = {
        'text': request.form['text'],
        'username': '%s (echobot)' % request.form['user_name'],
        'icon_emoji': 'splurge', # invalid, basically 'use default slack icon'
    }
    requests.post(endpoint, data=json.dumps(payload), headers=headers)
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    if endpoint is None:
        exit('Must set SLACK_WEBHOOK')
    app.run(host='0.0.0.0', port=3246)
