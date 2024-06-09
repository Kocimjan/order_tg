import telebot
from handlers.start_handler import start_handler
from handlers.registration_handler import registration_handler
from handlers.login_handler import login_handler

API_TOKEN = 'YOUR_API_TOKEN_HERE'
bot = telebot.TeleBot(API_TOKEN)

# Регистрация обработчиков
start_handler(bot)
registration_handler(bot)
login_handler(bot)

# Запуск бота
if __name__ == "__main__":
    bot.polling()
