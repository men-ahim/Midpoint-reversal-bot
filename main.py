from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "7236698037:AAHxUO1llSo5KXbvuMJIv3klEaE9g5yiUPU"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print("📩 Данные от Telegram:", data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={
                "chat_id": chat_id,
                "text": "✅ Бот успешно работает и получил ваш /start"
            })

    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Midpoint Reversal Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
