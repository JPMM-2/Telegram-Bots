
#   AQUI VAMOS A EXPLORAR COMO INTERACTUAR CON BOTONES

from config import *
import telebot
from telebot.types import ReplyKeyboardMarkup # para crear botones
from telebot.types import ForceReply # para citar unj mensaje
from telebot.types import ReplyKeyboardRemove # para eliminar botones
from random import randint

bot = telebot.TeleBot(TELEGRAM_TOKEN)

usuarios = {}

# mandamos una contestacion a los mesages que contienes "/"+ alguna de las palabras
@bot.message_handler(commands=['start','hola','buenas','que pasa bro'])
def cmd_start(message):
    markup = ReplyKeyboardRemove()
    bot.send_message(message.chat.id,'Usa el comando /jugar para empezar a jugar', reply_markup = markup)
