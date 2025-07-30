import telebot
from flask import Flask
import threading
import time

# === Токен бота ===
TOKEN = "7236698037:AAHxUO1llSo5KXbvuMJIv3klEaE9g5yiUPU"
bot = telebot.TeleBot(TOKEN)

# === Команда старт ===
@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот стратегии Midpoint Reversal. Скоро начну отправлять сигналы 📈")

# === Пример логики (заглушка, пока не добавим логику Midpoint Reversal) ===
def check_market_and_send_signals():
    while True:
        # Здесь будет логика анализа монет и сигналов
        # Пример: bot.send_message(chat_id, "Сигнал: LONG по BTCUSDT")
        time.sleep(60)  # Проверка каждую минуту (заглушка)

# === Flask для Render — чтобы приложение не завершалось ===
app = Flask(__name__)

@app.route("/")
def index():
    return "Midpoint Reversal Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    # Запуск Flask в отдельном потоке
    threading.Thread(target=run_flask).start()

    # Запуск телеграм-бота в отдельном потоке
    threading.Thread(target=bot.infinity_polling, name="telegram").start()

    # Запуск заглушки анализа сигналов
    threading.Thread(target=check_market_and_send_signals, name="signals").start()
