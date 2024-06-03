# module_alta.py
from telebot import types

def handle_alta(bot):
    user_data = {}

    def ask_name(message):
        msg = bot.send_message(message.chat.id, "Please enter your name:")
        bot.register_next_step_handler(msg, process_name_step)

    def process_name_step(message):
        try:
            user_data['name'] = message.text
            msg = bot.send_message(message.chat.id, "Please enter your age (18-130):")
            bot.register_next_step_handler(msg, process_age_step)
        except Exception as e:
            bot.send_message(message.chat.id, 'Something went wrong. Please try again.')

    def process_age_step(message):
        try:
            age = int(message.text)
            if 18 <= age <= 130:
                user_data['age'] = age
                markup = types.InlineKeyboardMarkup()
                btn_male = types.InlineKeyboardButton(text='Male', callback_data='gender_male')
                btn_female = types.InlineKeyboardButton(text='Female', callback_data='gender_female')
                btn_other = types.InlineKeyboardButton(text='Other', callback_data='gender_other')
                markup.add(btn_male, btn_female, btn_other)
                bot.send_message(message.chat.id, "Please select your gender:", reply_markup=markup)
            else:
                msg = bot.send_message(message.chat.id, "Age must be between 18 and 130. Please enter your age again:")
                bot.register_next_step_handler(msg, process_age_step)
        except ValueError:
            msg = bot.send_message(message.chat.id, "Invalid age. Please enter a number between 18 and 130:")
            bot.register_next_step_handler(msg, process_age_step)

    @bot.callback_query_handler(func=lambda call: call.data.startswith('gender_'))
    def process_gender_step(call):
        user_data['gender'] = call.data.split('_')[1]
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"Registration complete.\nName: {user_data['name']}\nAge: {user_data['age']}\nGender: {user_data['gender'].capitalize()}")

    @bot.message_handler(commands=['alta'])
    def send_alta(message):
        ask_name(message)
