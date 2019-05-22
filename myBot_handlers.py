import myBot_data as data
import locator_func as lf
import ass_func as af
import additional_func as adf
import ddos_func as df
import cryptography_func as cf
from myBot_main import bot


@bot.message_handler(commands=['start'])
@bot.edited_message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    msg = data.greetings
    bot.send_message(chat_id, msg)


@bot.message_handler(commands=['search'])
@bot.edited_message_handler(commands=['search'])
def handle_search(message):
    lf.search_game(message)


@bot.message_handler(commands=['ass_kraft'])
@bot.edited_message_handler(commands=['ass_kraft'])
def handle_ass_kraft(message):
    if adf.check_new_day():
        data.today = adf.get_date()
        adf.save_new_time_in_file()
        af.set_all_users_not_played_today()
    if not af.register_and_allow_play_game(message):
        af.send_user_played_today(message)
        return
    ass_progress = af.ass_width_upgrade(message)
    if af.check_ass_absence(message):
        af.set_ass_width_0(message)
        af.send_ass_absence(message)
        return
    af.send_result_of_game(message, ass_progress)
    adf.save_stats_in_file(data.file_of_ass_stats, data.users_in_ass_game)


@bot.message_handler(commands=['wides_ass_list'])
@bot.edited_message_handler(commands=['wides_ass_list'])
def handle_top_players(message):
    if af.check_users_absence_in_chat(message):
        af.send_users_absence_in_chat(message)
        return
    af.send_wides_ass_list(message)


@bot.message_handler(commands=['my_ass_width'])
@bot.edited_message_handler(commands=['my_ass_width'])
def handle_my_ass_width(message):
    if af.check_user_not_in_game(message):
        af.send_user_not_in_game(message)
        return
    af.send_ass_width(message)


@bot.message_handler(commands=['ddos_on'])
@bot.edited_message_handler(commands=['ddos_on'])
def handle_ddos_on(message):
    if not df.check_valid_syntax(message):
        df.send_invalid_syntax(message)
        return
    username = df.get_username_from_text(message)
    personal_id = adf.make_personal_id(message, username)
    if personal_id not in data.users_ddos:
        data.users_ddos.append(personal_id)
        df.send_ddos_on(message)
        adf.save_stats_in_file(data.file_of_ddos_users, data.users_ddos)


@bot.message_handler(commands=['ddos_off'])
@bot.edited_message_handler(commands=['ddos_off'])
def handle_ddos_off(message):
    if not df.check_valid_syntax(message):
        df.send_invalid_syntax(message)
        return
    username = df.get_username_from_text(message)
    personal_id = adf.make_personal_id(message, username)
    if personal_id in data.users_ddos:
        data.users_ddos.remove(personal_id)
        df.send_ddos_off(message)
        adf.save_stats_in_file(data.file_of_ddos_users, data.users_ddos)


@bot.message_handler(commands=['encrypt'])
@bot.edited_message_handler(commands=['encrypt'])
def handle_encrypt(message):
    text = message.text
    content = text.splitlines()
    if not cf.check_valid(content):
        cf.send_encrypt_rules(message)
        return
    cf.send_encrypt(message, content)


@bot.message_handler(commands=['tell_new_name'])
@bot.edited_message_handler(commands=['tell_new_name'])
def handle_new_name(message):
    user_name = message.from_user.first_name
    chat_id = message.chat.id
    user_id = message.from_user.id
    bot.send_message(chat_id, f"{user_name}, ваше ім'я в рейтингу оновлено!")
    data.users_in_ass_game[chat_id][user_id][0] = user_name
    adf.save_stats_in_file(data.file_of_ass_stats, data.users_in_ass_game)

"""
@bot.message_handler(content_types=['sticker'])
def handle_text(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
"""

@bot.message_handler(content_types=['text', 'sticker', 'photo', 'video', 'audio', 'document', 'voice'])
@bot.edited_message_handler(content_types=['text', 'sticker', 'photo', 'video', 'audio', 'document', 'voice'])
def handle_text(message):
    if message.content_type == 'text':
        # adf.save_conversation_in_file(message, data.file_of_txt_messages)
        if message.chat.id == -1001490612040:
            adf.troll_ruslan(message)
    df.ddos(message)
