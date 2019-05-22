from myBot_main import bot
import myBot_data as data
import datetime
import pytz

file_encoding = 'utf8'

def send_troll_ruslan(message):
    msg = data.troll_ruslan_phrase
    bot.reply_to(message, msg)


def troll_ruslan(message):
    for name in data.ruslic:
        if name.lower() in message.text.lower():
            send_troll_ruslan(message)
            return


def make_personal_id(message, additional_info):
    chat_id = message.chat.id
    return f'{chat_id}_{additional_info}'


def save_new_time_in_file():
    date = get_date()
    save_stats_in_file(data.file_of_date, date)

"""
def save_conversation_in_file(message, outp):
    with open(outp, 'a', encoding=file_encoding) as file:
        file.write(f'{datetime.datetime.now()}; \t')
        file.write(f'id = {message.from_user.id}; \t')
        file.write(f'chat_id = {message.chat.id};\n')

        if message.from_user.first_name is not None:
            file.write(f' \tname = {message.from_user.first_name} ')

        if message.from_user.last_name is not None:
            file.write(f'{message.from_user.last_name};')

        file.write(f' \n\tmsg = [{message.text}]; \n')
"""

def save_stats_in_file(file, info):
    delete_first_two_lines_in_file(file)
    with open(file, 'a', encoding=file_encoding) as f:
        buf = f'{datetime.datetime.now()} \n{info} \n'
        f.write(buf)


def read_last_line_of_file(file):
    with open(file, 'r', encoding=file_encoding) as f:
        info = f.readlines()[-1].strip(' \n')
        return info


def clear_file(file, new_content):
    with open(file, 'w', encoding=file_encoding):
        file.clear()
        file.write(new_content)


def delete_first_two_lines_in_file(file):
    with open(file,'r', encoding=file_encoding) as f:
        all = f.readlines()
    all.pop(0)
    all.pop(0)
    with open(file,'w', encoding=file_encoding) as f:
        f.writelines(all)


def check_new_day():
    return data.today != get_date()


def get_time_of_last_call():
    return read_last_line_of_file(data.file_of_date)


def get_date():
    return str(datetime.datetime.now(pytz.timezone('europe/kiev'))).split('-')[2].split()[0]
