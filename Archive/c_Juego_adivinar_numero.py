
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

@bot.message_handler(commands = ['jugar'])
def cmd_jugar(message):
    numero = randint(1,10)
    print (numero)
    cid = message.chat.id
    usuarios[cid] = numero
    botones = ReplyKeyboardMarkup(input_field_placeholder = 'Pulsa un boton')
    botones.add('1','2','3','4','5','6','7','8','9','10')
    msg = bot.send_message(message.chat.id, 'Adivina el numero', reply_markup = botones)   
    bot.register_next_step_handler(msg, comprobar_numero)
    
    
def comprobar_numero(message):
    cid = message.chat.id
    if not message.text.isdigit():
        msg = bot.send_message(message.chat.id, 'Error: elige un numero')
        bot.register_next_step_handler(msg, comprobar_numero)
    else:
        n = int(message.text)
        if n<1 or n>10:
            msg = bot.send_message(message.chat.id, 'Error: fuera de rango')
            bot.register_next_step_handler(msg, comprobar_numero)
        else:
            if n == usuarios[cid]:
                markup = ReplyKeyboardRemove()
                bot.send_message(message.chat.id, 'perfecto!!', reply_markup = markup)
                # damos la opcion de jugar otra vez
                botones = ReplyKeyboardMarkup(input_field_placeholder = 'quieres jugar otra vez?')
                botones.add('otra vez', 'no gracias')
                msg = bot.send_message(message.chat.id, 'jugar otra vez?', reply_markup = botones) 
                bot.register_next_step_handler(msg, seguir)
            else:
                msg = bot.send_message(message.chat.id, 'Incorrecto')
                bot.register_next_step_handler(msg, comprobar_numero)

def seguir(message):
    if message.text == 'otra vez':
        cmd_jugar(message)
        #markup = ReplyKeyboardRemove()
        #bot.send_message(message.chat.id, 'usa el comando /jugar para empezar de nuevo', reply_markup = markup)
    else:
        markup = ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Gracias por mparticipar', reply_markup = markup)


#   MAIN LOOP

if __name__ == '__main__':
    print ('iniciando bot')
    bot.infinity_polling()
    print('Fin')

