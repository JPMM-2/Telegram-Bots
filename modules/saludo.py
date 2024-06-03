# module_borrar.py
import sqlite as sql
from telebot import types
import alta 
import servicios



'''
def handle_saludar(bot):
    
    @bot.message_handler(commands=['start'])
    def send_saludar(message):
        name = sql.exists(message.chat.id)
        if name:
            bot.send_message(message.chat.id, 'welcome ' + name)        
            markup = types.InlineKeyboardMarkup()
            btn_servicios = types.InlineKeyboardButton(text='Servicios', callback_data='saludo_servicios')
            btn_facebook = types.InlineKeyboardButton(text='Facebook', callback_data='saludo_facebook')
            btn_cita = types.InlineKeyboardButton(text='Pedir cita', callback_data='saludo_cita')
            markup.add(btn_servicios, btn_facebook, btn_cita)
            msg = bot.send_message(message.chat.id, "How I can help you??", reply_markup=markup)
            servicios.handle_servicios(bot)
        else:
            bot.send_message(message.chat.id, 'Usa el comando /alta para registrarte y continuar')
            bot.register_next_step_handler(message, alta.handle_alta) 
'''

def handle_saludar(bot):
    
    @bot.message_handler(commands=['start'])
    def send_saludar(message):
        name = sql.exists(message.chat.id)
        if name:
            bot.send_message(message.chat.id, 'welcome ' + name)        
            markup = types.InlineKeyboardMarkup()
            btn_servicios = types.InlineKeyboardButton(text='Servicios', callback_data='saludo_servicios')
            btn_facebook = types.InlineKeyboardButton(text='Facebook', url='https://www.facebook.com/ARTNAILSGETXO/?locale=es_ES')
            btn_cita = types.InlineKeyboardButton(text='Pedir cita', url='https://jpnails.trafft.com/booking')
            markup.add(btn_servicios, btn_facebook, btn_cita)
            msg = bot.send_message(message.chat.id, "How I can help you??", reply_markup=markup)
            servicios.handle_servicios(bot)
        else:
            bot.send_message(message.chat.id, 'Usa el comando /alta para registrarte y continuar')
            bot.register_next_step_handler(message, alta.handle_alta) 