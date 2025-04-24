from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_alert():
    data = request.get_json(force=True)

    # Log to Railway console
    print("🚨 New Alert Received")
    print("Timestamp:", datetime.utcnow().isoformat())
    print(json.dumps(data, indent=4))  # Pretty print

    return jsonify({"status": "ok", "received": data}), 200

@app.route('/', methods=['GET'])
def hello():
    return "👋 Garland Webhook is alive and waiting for signals!", 200
