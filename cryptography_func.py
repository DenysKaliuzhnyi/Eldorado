from myBot_main import bot


def encode(text, _from, _to):
    print(_from, _to)
    return text.translate(str.maketrans(_from, _to))


def check_valid(content):
    return len(content) == 4 and len(content[2]) == len(content[3])


def str_encrypt_rules():
    return 'команда має структуру: \n' \
            'рядок1: /enctypt \n' \
            'рядок2: повідомлення, яке шифруємо \n' \
            'рядок3: символи, які будуть замінені \n' \
            'рядок4: символи, на які замінюємо \n' \
            'кожний символ з 3го рядка відповідає символу з 4го по ' \
            'стовпчикам. Тобто, довжина 3го і 4го рядків має бути однакова'


def str_encrypted_msg(encoded):
    return 'ваше закодоване повідомлення: \n' + encoded


def send_encrypt_rules(message):
    chat_id = message.chat.id
    msg = str_encrypt_rules()
    bot.send_message(chat_id, msg)


def send_encrypt(message, content):
    chat_id = message.chat.id
    skip, _text, _from, _to = content
    encoded = encode(_text, _from, _to)
    msg = str_encrypted_msg(encoded)
    bot.send_message(chat_id, msg)
