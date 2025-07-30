from flask import Flask, request
import requests
import time

app = Flask(__name__)

BOT_TOKEN = "7236698037:AAHxUO1llSo5KXbvuMJIv3klEaE9g5yiUPU"
CHAT_ID = None  # будет определён при первом /start

@app.route("/")
def index():
    return "Midpoint Reversal Bot is running!"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def receive_update():
    global CHAT_ID
    data = request.get_json()

    if "message" in data:
        message = data["message"]
        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        if text == "/start":
            CHAT_ID = chat_id
            send_message("✅ Бот успешно запущен и готов к работе.")
        else:
            send_message(f"Вы написали: {text}")

    return {"ok": True}

def send_message(text):
    if CHAT_ID:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": text}
        requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
