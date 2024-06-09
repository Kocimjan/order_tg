from telebot import TeleBot, types
from db import register_user

def registration_handler(bot: TeleBot):
    @bot.callback_query_handler(func=lambda call: call.data == "register")
    def callback_register(call):
        msg = bot.send_message(call.message.chat.id, "Введите имя пользователя:")
        bot.register_next_step_handler(msg, process_register_username_step)

    def process_register_username_step(message):
        username = message.text
        msg = bot.send_message(message.chat.id, "Введите email:")
        bot.register_next_step_handler(msg, process_register_email_step, username)

    def process_register_email_step(message, username):
        email = message.text
        msg = bot.send_message(message.chat.id, "Введите пароль:")
        bot.register_next_step_handler(msg, process_register_password_step, username, email)

    def process_register_password_step(message, username, email):
        password = message.text
        if register_user(username, email, password):
            bot.send_message(message.chat.id, "Регистрация прошла успешно!")
        else:
            bot.send_message(message.chat.id, "Ошибка регистрации. Пользователь с таким именем или электронной почтой уже существует.")
