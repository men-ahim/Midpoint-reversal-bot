import os
import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

@app.route("/")
def index():
    return "Midpoint Reversal Bot is running!"

@app.route("/signal", methods=["POST"])
def signal():
    content = request.json
    message = f"Signal: {content}"
    send_telegram_message(message)
    return "OK"
