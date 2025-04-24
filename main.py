from flask import Flask, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_alert():
    data = request.json
    print("✅ Alert received:", data)

    # Save to local file (in Railway container for test)
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    filename = f"signal_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump(data, f)

    return jsonify({"status": "ok", "received": data}), 200

@app.route('/', methods=['GET'])
def hello():
    return "Garland Webhook Ready 👋", 200
