from myBot_main import bot
import myBot_data as data
import random
import math

''' REGISTER ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''


def register_and_allow_play_game(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if chat_id not in data.users_in_ass_game:                                        # register chat
        register_new_chat(message)
    if user_id in data.users_in_ass_game[chat_id]:
        if check_user_played_today(message):                                      # if user played today
            return False
    else:                                                                            # register user
        register_new_user(message)
        send_user_is_registered(message)
    set_user_played_today(message)
    return True


def register_new_chat(message):
    chat_id = message.chat.id
    data.users_in_ass_game.update({chat_id: {}})


def register_new_user(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chat_id = message.chat.id
    data.users_in_ass_game[chat_id].update({user_id: [user_name, 0, True]})


''' SEND ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''


def send_user_not_in_game(message):
    chat_id = message.chat.id
    msg = str_user_not_in_game()
    bot.send_message(chat_id, msg)


def send_result_of_game(message, ass_progress):
    chat_id = message.chat.id
    str_event = str_event_with_ass(ass_progress)
    msg = str_result_of_game(message, str_event, ass_progress)
    bot.send_message(chat_id, msg)


def send_ass_width(message):
    msg = str_personal_ass_stats(message)
    bot.reply_to(message, msg)


def send_users_absence_in_chat(message):
    chat_id = message.chat.id
    msg = str_users_absence_in_chat()
    bot.send_message(chat_id, msg)


def send_user_is_registered(message):
    chat_id = message.chat.id
    msg = str_user_is_registered(message)
    bot.send_message(chat_id, msg)


def send_user_played_today(message):
    msg = str_user_played_today(message)
    bot.reply_to(message, msg)


def send_wides_ass_list(message):
    chat_id = message.chat.id
    sorted_users = sort_players_by_width(message)
    top = str_top_players(sorted_users)
    bot.send_message(chat_id, top)


def send_ass_absence(message):
    chat_id = message.chat.id
    msg = ass_absence_str(message)
    bot.send_message(chat_id, msg)


''' SET ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''


def set_user_played_today(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    data.users_in_ass_game[chat_id][user_id][2] = True


def set_all_users_not_played_today():
    for chat_id, chat_info in data.users_in_ass_game.items():
        for user_id, user_info in chat_info.items():
            user_info[2] = False


def set_ass_width_0(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    data.users_in_ass_game[chat_id][user_id][1] = 0


''' CHECK ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''


def check_user_played_today(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    return data.users_in_ass_game[chat_id][user_id][2]


def check_user_not_in_game(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    return chat_id not in data.users_in_ass_game or user_id not in data.users_in_ass_game[chat_id]


def check_users_absence_in_chat(message):
    chat_id = message.chat.id
    return chat_id not in data.users_in_ass_game


def check_ass_absence(message):
    return get_ass_width(message) <= 0


''' STRINGS ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''


def str_result_of_game(message, str_event, ass_progress):
    user_name = message.from_user.first_name
    return f'{user_name}, твоє очко {str_event} на {abs(ass_progress)} см, тепер його діаметр: {get_ass_width(message)}'


def str_user_not_in_game():
    return 'ти ще не грав!'


def str_users_absence_in_chat():
    return f'гравців ще немає!'


def ass_absence_str(message):
    user_name = message.from_user.first_name
    return f'{user_name}, в тебе немає очка'


def str_user_is_registered(message):
    user_name = message.from_user.first_name
    return f'{user_name}, ти зареєструвався у грі \"найширше очко\"'


def str_user_played_today(message):
    user_name = message.from_user.first_name
    return f'{user_name}, {random.choice(data.phrases_ignore_ass)}'


def str_personal_ass_stats(message):
    width = get_ass_width(message)
    return f'наразі ширина твого очка складає {width} см.'


def str_top_players(sorted_users):
    str_top = f'Топ рейтинг очкозаврів: \n'
    n = 1
    for user_id, info in sorted_users.items():
        str_top += f'{n}. {info[0]} має очко завширшки {info[1]} см. \n'
        n += 1
    return str_top


def str_event_with_ass(num):
    if num >= 0:
        return 'розширилось'
    else:
        return 'звузилось'


''' GET ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''


def get_chat(message):
    chat_id = message.chat.id
    return data.users_in_ass_game[chat_id]


def get_user(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    return data.users_in_ass_game[chat_id][user_id]


def get_ass_width(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    return data.users_in_ass_game[chat_id][user_id][1]


''' OTHER ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''


def rand_ass_width():
    num = 0
    while num == 0:
        num = round(random.gauss(1, math.sqrt(15)))
    return num


def ass_width_upgrade(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    num = rand_ass_width()
    data.users_in_ass_game[chat_id][user_id][1] += num
    return num


def sort_players_by_width(message):
    chat_id = message.chat.id
    return dict(sorted(data.users_in_ass_game[chat_id].items(), key=lambda el: el[1][1], reverse=True))





