
from config import *
import nails_shop as mm 
import telebot

bot = telebot.TeleBot(TELEGRAM_TOKEN)

mm.mainn(bot)







