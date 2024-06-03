# module_borrar.py
from button_class import InlineButtonHandler

def handle_borrar(bot):
    button_handler = InlineButtonHandler(bot)

    @bot.message_handler(commands=['borrar'])
    def send_borrar(message):
        question, markup = button_handler.create_buttons("Are you sure?", yes_text="Yes", no_text="No")
        bot.send_message(message.chat.id, question, reply_markup=markup)
