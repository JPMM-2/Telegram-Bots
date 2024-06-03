# main.py
import telebot
from module_borrar import handle_borrar
from alta import handle_alta

from config import *

API_TOKEN = 'YOUR_API_TOKEN'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Register the handlers from the modules
handle_borrar(bot)
handle_alta(bot)

# Start polling
bot.polling()
