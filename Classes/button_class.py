# inline_button_handler.py
import telebot
from telebot import types

class InlineButtonHandler:
    def __init__(self, bot):
        self.bot = bot
        self.bot.callback_query_handler(func=lambda call: call.data.startswith('confirm_'))(self.callback_confirm)

    def create_buttons(self, question, yes_text='Yes', no_text='No', yes_callback='yes', no_callback='no'):
        markup = types.InlineKeyboardMarkup()
        btn_yes = types.InlineKeyboardButton(text=yes_text, callback_data=f'confirm_{yes_callback}')
        btn_no = types.InlineKeyboardButton(text=no_text, callback_data=f'confirm_{no_callback}')
        markup.add(btn_yes, btn_no)
        return question, markup

    def callback_confirm(self, call):
        if call.data == 'confirm_yes':
            self.bot.answer_callback_query(call.id, "Confirmed!")
            self.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Confirmed!", reply_markup=None)
        elif call.data == 'confirm_no':
            self.bot.answer_callback_query(call.id, "Cancelled!")
            self.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Cancelled!", reply_markup=None)
