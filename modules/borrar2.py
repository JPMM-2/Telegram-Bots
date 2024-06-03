# module_borrar.py
import sqlite as sql
from telebot import types

def handle_borrar(bot):
    @bot.message_handler(commands=['borrar'])
    def send_borrar(message):
        markup = types.InlineKeyboardMarkup()
        btn_yes = types.InlineKeyboardButton(text='Yes', callback_data='borrar_yes')
        btn_no = types.InlineKeyboardButton(text='No', callback_data='borrar_no')
        markup.add(btn_yes, btn_no)
        bot.send_message(message.chat.id, "Are you sure?", reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: call.data.startswith('borrar_'))
    def callback_borrar(call):
        try:
            if call.data == 'borrar_yes':
                sql.delete(call.message.chat.id)
                bot.answer_callback_query(call.id, "Confirmed!")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Delete Confirmed!", reply_markup=None)
            elif call.data == 'borrar_no':
                bot.answer_callback_query(call.id, "Cancelled!")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Delete Cancelled!", reply_markup=None)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
