

from telebot import types

def handle_options(bot):
    
    @bot.callback_query_handler(func=lambda call: call.data.startswith('saludo_'))
    def callback_query(call):
        if call.data == 'saludo_servicios':
            # Send a picture
            bot.send_photo(call.message.chat.id, photo=open('servicios.jpeg', 'rb'))
        elif call.data == 'saludo_facebook':
            # Send a URL
            bot.send_message(call.message.chat.id, 'https://www.facebook.com')
        elif call.data == 'saludo_cita':
            # Send a message
            bot.send_message(call.message.chat.id, 'hello bro')


