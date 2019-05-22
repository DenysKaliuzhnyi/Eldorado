from flask import Flask
from flask import request
from flask_sslify import SSLify
import telebot
import time
import myBot_token

TOKEN = myBot_token.TOKEN_2
bot = telebot.TeleBot(TOKEN, threaded=False)


app = Flask(__name__)
sslify = SSLify(app)


bot.remove_webhook()
time.sleep(1)
bot.set_webhook(f'https://deniskakoderpro007.pythonanywhere.com/{TOKEN}')


import myBot_handlers

@app.route('/', methods=["GET"])
def GET():
    return "<h1>I'm working :)</h1>"


@app.route(f'/{TOKEN}', methods=["POST"])
def POST():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "ok", 200


if __name__ == '__main__':
    app.run()
