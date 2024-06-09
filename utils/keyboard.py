from telebot import types

def get_main_menu():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Регистрация", callback_data="register"))
    markup.add(types.InlineKeyboardButton("Авторизация", callback_data="login"))
    return markup
