from flask import Flask, request
from flask_cors import CORS
from datetime import datetime, timedelta
import json
import os
import string
import random

basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'static/scores.json')

players=[]
session_key = ""
session_key_valid_until = datetime.now()

with open(data_file, mode="r", encoding="utf-8") as playersfile:
    players = json.load(playersfile)

app = Flask(__name__)
cors = CORS(app)

@app.route('/api/login', methods=['POST', 'OPTIONS'])
def login():
    global session_key, session_key_valid_until
    data = request.get_json(force=True)
    username = data['username']
    password = data['password']
    if (username == 'admin' and password == 'SVL1920'):
        session_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=24))
        session_key_valid_until = datetime.now() + timedelta(hours=3)
        print(session_key)
        return session_key, 200
    return "", 403

@app.route("/api/currentMonth")
def get_current_month():
    with open(data_file, mode="r", encoding="utf-8") as scoresfile:
        scores = json.load(scoresfile)
        return [x for x in scores if x['monthIndex'] == datetime.now().month], 200

@app.route("/api/all")
def get_all():
    with open(data_file, mode="r", encoding="utf-8") as scoresfile:
        return json.load(scoresfile), 200

@app.route('/api/auth', methods=['POST', 'OPTIONS'])
def check_auth():
    global session_key, session_key_valid_until
    data = request.get_json(force=True)
    sk = data['sessionKey']
    if (sk != session_key or session_key_valid_until <= datetime.now()):
        return ""
    return session_key

@app.route('/api/update', methods=['POST', 'OPTIONS'])
def update():
    global session_key, session_key_valid_until
    data = request.get_json(force=True)
    sk = data['sessionKey']
    if (sk != session_key or session_key_valid_until <= datetime.now()):
        return False, 403
    month = { "monthIndex": datetime.now().month, "players": data['players']}
    with open(data_file, mode="r", encoding="utf-8") as scoresfile:
        scores = json.load(scoresfile)
        otherMonths = [x for x in scores if x['monthIndex'] != datetime.now().month]
        otherMonths.append(month)
    with open(data_file, mode="w", encoding="utf-8") as scoresfile:
        json.dump(otherMonths, scoresfile)
        return month, 200