
# main.py
import telebot
from borrar2 import handle_borrar
from alta3 import handle_alta
from saludo import handle_saludar

from servicios import handle_servicios 

from config import *

API_TOKEN = 'YOUR_API_TOKEN'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

try:

    # Register the handlers from the modules
    handle_saludar(bot)
    handle_borrar(bot)
    handle_alta(bot)
    handle_servicios(bot)

    # Start polling
    bot.polling()
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
