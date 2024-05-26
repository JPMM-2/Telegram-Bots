
#  EN ESTE SCRIUPT MANDAMOS MENSAGES, LOS CAMBIAMOS Y LOS BORRAMOS
#  TAMBIEN PONEMOS TRIGGERS PARA UN MENSAGE O PARA OTRO

# youtube link https://www.youtube.com/watch?v=TLtnXAWFUQg&list=PLheIVUbpfWZ2wDRHulCcuIVF-9lkIvyBi&index=1

from config import *
import telebot
import time
import threading

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# contestamos a un mensage con referencia al mensage
@bot.message_handler(commands=['reply'])
def cmd_start(message):
    bot.reply_to(message,'hello bro reply')

# mandamos una contestacion a los mesages que contienes "/"+ alguna de las palabras
@bot.message_handler(commands=['hola','buenas','que pasa bro'])
def cmd_start(message):
    bot.send_message(message.chat.id,'hello bro normal msg')


# PARTE IMPORTANTE DE MODIFICAR/BORRAR TEXTO
# mandamos un mensage a cada mensage que recibamos tipo texto
# damos formato basado en MARKDOWN  

@bot.message_handler(content_types = ['text'])
def bot_message_texto(message):
    # damos formato con markdown
    text_md = '*este mensage esta en negrita*' + '\n'
    if message.text.startswith('/'):
        bot.send_message(message.chat.id,'Comando no disponible')
    else:
        print (message.chat.id)
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(3)
        x = bot.send_message(message.chat.id,text_md,parse_mode = 'MarkdownV2', disable_web_page_preview = True)
        y = bot.send_message(message.chat.id,'__este mensage esta subrayado__',parse_mode = 'MarkdownV2', disable_web_page_preview = False)
        bot.send_message(message.chat.id,'Como estan los makinas')
        # aqui cambiamos el mensage x de "este mensage esta en negrita" a "este mensage esta en negrita cambiado"
        time.sleep(3)
        bot.edit_message_text('*este mensage esta en negrita cambiado*', message.chat.id, x.message_id, parse_mode = 'MarkdownV2')
        # aqui borramos el mensage "este mensage esta subrayado"
        time.sleep(3)
        bot.delete_message(message.chat.id, y.message_id)

'''

# aqui cambiamos un mensage 
# aqui tratamos el resto de mensages de texto
@bot.message_handler( content_types = ['text'])
def bot_message_texto2(message):
    # damos formato con markdown
    text_md = '*este mensage va a cambiar*' + '\n'
    if message.text.startswith('/'):
        bot.send_message(message.chat.id,'Comando no disponible')
    else:
        x = bot.send_message(message.chat.id,text_md,parse_mode = 'MarkdownV2', disable_web_page_preview = True)
        time.sleep(3)
        bot.edit_message_text('__cambiado__', message.chat.id, x.message_id)
'''


def recibir_msg():
    bot.infinity_polling()


if __name__ == '__main__':
    print ('iniciando bot')
    hilo_bot = threading.Thread(name = 'hilo_bot', target = recibir_msg)
    hilo_bot.start()
    print('Fin')


