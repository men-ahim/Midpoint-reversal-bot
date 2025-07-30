from flask import Flask, request
import requests

TOKEN = "7236698037:AAHxUO1llSo5KXbvuMJIv3klEaE9g5yiUPU"
URL = f"https://api.telegram.org/bot{TOKEN}"

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Midpoint Reversal Bot is running!"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if text == "/start":
            requests.post(f"{URL}/sendMessage", json={
                "chat_id": chat_id,
                "text": "✅ Бот запущен и работает!"
            })
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
