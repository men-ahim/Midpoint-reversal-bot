from flask import Flask
import requests
import time
import os

app = Flask(__name__)

TELEGRAM_TOKEN = "7236698037:AAHxUO1llSo5KXbvuMJIv3klEaE9g5yiUPU"
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "self")  # 'self' отправляет самому себе

@app.route("/")
def index():
    return "Midpoint Reversal Bot is running!"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

if __name__ == "__main__":
    send_telegram_message("✅ Midpoint Reversal Bot запущен!")
    app.run(host="0.0.0.0", port=10000)
