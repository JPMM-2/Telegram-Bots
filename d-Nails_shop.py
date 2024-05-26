from config import *
import telebot
from telebot.types import ReplyKeyboardMarkup # para crear botones
from telebot.types import ForceReply # para citar unj mensaje
from telebot.types import ReplyKeyboardRemove # para eliminar botones

import b_cuestionario_new_users_MODULE as new

import sqlite as sql

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# aqui guardamos datos de usuario
users = {}


# mandamos una contestacion a los mesages que contienes "/"+ alguna de las palabras
@bot.message_handler(commands=['start','hola','buenas','que pasa bro'])
def cmd_start(message):
    markup = ReplyKeyboardRemove()
    bot.send_message(message.chat.id,'Usa el comando /start para empezar a jugar', reply_markup = markup)
    print (message.chat.id)
    name = sql.exists(message.chat.id)
    if name:
        bot.send_message(message.chat.id, 'welcome ' + name)
    else:
        msg = bot.send_message(message.chat.id, 'bienvenida nueva clienta')
        new.cmd_alta(msg)


#   MAIN LOOP
if __name__ == '__main__':
    print ('iniciando bot')
    bot.infinity_polling()
    print('Fin')
