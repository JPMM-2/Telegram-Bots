

# main.py
import telebot

from start import handle_saludar

from config import *

API_TOKEN = 'YOUR_API_TOKEN'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Register the handlers from the modules
handle_saludar(bot)


# Start polling
bot.polling()
