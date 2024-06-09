from telebot import TeleBot
from utils.keyboard import get_main_menu

def start_handler(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, "Добро пожаловать! Выберите действие:", reply_markup=get_main_menu())
