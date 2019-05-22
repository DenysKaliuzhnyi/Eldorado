from myBot_main import bot
import additional_func as adf
import myBot_data as data


def ddos(message):
    username = message.from_user.username
    personal_id = adf.make_personal_id(message, username)
    if personal_id in data.users_ddos:
        send_ddos(message)


def get_username_from_text(message):
    return message.text.split('[')[1].split(']')[0].strip(' ').replace('@', '')


def send_ddos(message):
    msg = data.ddos_phrase
    bot.reply_to(message, msg)


def send_ddos_on(message):
    chat_id = message.chat.id
    username = get_username_from_text(message)
    msg = f'увімкнено ddos-режим на @{username}'
    bot.send_message(chat_id, msg)


def send_ddos_off(message):
    chat_id = message.chat.id
    username = get_username_from_text(message)
    msg = f'вимкнено ddos-режим на @{username}'
    bot.send_message(chat_id, msg)


def send_invalid_syntax(message):
    chat_id = message.chat.id
    msg = 'команда має структуру: /ddos_on (або off) [username] \n' \
          'у квадратних дужках вказується юзернейм того, кого (не) дудосити'
    bot.send_message(chat_id, msg)


def check_valid_syntax(message):
    content = message.text
    return content.count('[') == 1 and content.count(']') == 1 and content.find('[') < content.find(']')


def save_ddos_users_in_file():
    with open(data.file_of_ddos_users, 'a', encoding='utf32') as file:
        file.write(str(data.users_ddos))
        file.write('\n')