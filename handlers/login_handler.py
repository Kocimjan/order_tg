from telebot import TeleBot, types
from db import login_user

def login_handler(bot: TeleBot):
    @bot.callback_query_handler(func=lambda call: call.data == "login")
    def callback_login(call):
        msg = bot.send_message(call.message.chat.id, "Введите email:")
        bot.register_next_step_handler(msg, process_login_email_step)

    def process_login_email_step(message):
        email = message.text
        msg = bot.send_message(message.chat.id, "Введите пароль:")
        bot.register_next_step_handler(msg, process_login_password_step, email)

    def process_login_password_step(message, email):
        password = message.text
        user_id = login_user(email, password)
        if user_id:
            bot.send_message(message.chat.id, "Авторизация прошла успешно!")
        else:
            bot.send_message(message.chat.id, "Неверный email или пароль.")
