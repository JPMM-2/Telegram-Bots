
#   AQUI VAMOS A EXPLORAR COMO INTERACTUAR CON BOTONES

#   https://www.youtube.com/watch?v=3OHnn5gVbRQ&list=PLheIVUbpfWZ2wDRHulCcuIVF-9lkIvyBi&index=2

from config import *
import telebot
from telebot.types import ReplyKeyboardMarkup # para crear botones
from telebot.types import ForceReply # para citar unj mensaje
from telebot.types import ReplyKeyboardRemove # para eliminar botones
import threading

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# ==================================================================================
# ==================================================================================

# aqui guardamos datos de usuario
users = {}


# mandamos una contestacion a los mesages que contienes "/"+ alguna de las palabras
@bot.message_handler(commands=['start','hola','buenas','que pasa bro'])
def cmd_start(message):
    markup = ReplyKeyboardRemove()
    bot.send_message(message.chat.id,'Usa el comando /alta para introducir tus datos', reply_markup = markup)

   
@bot.message_handler(commands = ['alta'])
def cmd_alta(message):
    markup = ForceReply()
    name = bot.send_message(message.chat.id, 'Como te llamas?', reply_markup = markup)
    bot.register_next_step_handler(name, preguntar_edad)
    

def preguntar_edad(message):
    nombre = message.text
    print ('tu nombre es ' + nombre)
    users[message.chat.id] = {}
    users[message.chat.id]['nombre'] = message.text
    markup = ForceReply()
    age = bot.send_message(message.chat.id, 'Cual es tu edad?', reply_markup = markup)
    bot.register_next_step_handler(age, preguntar_genero)


def preguntar_genero(message):
    if not message.text.isdigit():
        markup = ForceReply()
        msg = bot.send_message(message.chat.id, 'ERROR: debes indicar un numero')
        bot.register_next_step_handler(msg, preguntar_genero)
    else:
        edad = message.text
        print ('tu edad es ' + edad)
        users[message.chat.id]['edad'] = int(message.text)
        markup = ReplyKeyboardMarkup(
            one_time_keyboard = True, 
            input_field_placeholder = 'Pulsa el boton',
            resize_keyboard = True)
        markup.add('Hombre','Mujer')
        gender = bot.send_message(message.chat.id, 'Cual es tu sexo?', reply_markup = markup)
        bot.register_next_step_handler(gender, final)

def final(message):
    if message.text != 'Hombre' and message.text != 'Mujer':
        msg = bot.send_message(message.chat.id, 'ERROR: debes pulsar un boton')
        bot.register_next_step_handler(msg, final)
    else:
#        markup = ReplyKeyboardRemove()
        gender = message.text
        print ('tu genero es ' + gender)
        users[message.chat.id]['gender'] = message.text
        print ('ahora printamos todo los datos /n')
        print (users[message.chat.id]['nombre'] + ' // ' + 'es tu nombre')
        print (str(users[message.chat.id]['edad']) + ' // ' + 'es tu edad')
        print (users[message.chat.id]['gender'] + ' // ' + 'es tu genero')
        markup = ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Gracias por confiar en nosotros', reply_markup = markup)


#   MAIN LOOP
def recibir_msg():
    bot.infinity_polling()


if __name__ == '__main__':
    print ('iniciando bot')
    hilo_bot = threading.Thread(name = 'hilo_bot', target = recibir_msg)
    hilo_bot.start()
    print('Fin')

