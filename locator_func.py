import myBot_data as data
from myBot_main import bot
import random


def str_search_game(user_name):
    return f'{random.choice(data.phrases_locator_1)} ' \
           f'\n{random.choice(data.phrases_locator_2)}' \
           f' \n{user_name}, {random.choice(data.phrases_locator_3)}'


def send_search_game(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name
    msg = str_search_game(user_name)
    bot.send_message(chat_id, msg)


def search_game(message):
    chat_id = message.chat.id
    coords = random.choice(data.centerts)
    send_search_game(message)
    bot.send_chat_action(chat_id, 'find_location')
    bot.send_location(chat_id, random_coordinate_lat(coords[0]), random_coordinate_long(coords[1]))


def random_coordinate_lat(coord):
    limit = 90
    num = 999999
    while abs(num) > limit:
        num = random.gauss(coord, limit/9)
    return num


def random_coordinate_long(coord):
    limit = 180
    num = 999999
    while abs(num) > limit:
        num = random.gauss(coord, limit/9)
    return num


