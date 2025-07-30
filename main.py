from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "7236698037:AAHxUO1llSo5KXbvuMJIv3klEaE9g5yiUPU"
CHAT_ID = None

@app.route("/", methods=["GET"])
def index():
    return "Midpoint Reversal Bot is running!"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    global CHAT_ID
    data = request.get_json()
    if "message" in data:
        CHAT_ID = data["message"]["chat"]["id"]
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            data={"chat_id": CHAT_ID, "text": "🤖 Bot is now active and listening!"},
        )
    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)