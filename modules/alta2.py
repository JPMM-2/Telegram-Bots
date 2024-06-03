# module_alta.py
from telebot import types
import sqlite as sql

def handle_alta(bot):
    user_data = {}

    def ask_name(message):
        user_data['username'] = message.from_user.first_name
        msg = bot.send_message(message.chat.id, "Please enter your name:")
        bot.register_next_step_handler(msg, process_name_step)
        print (msg.text)

    def process_name_step(message):
        try:
            user_data['name'] = message.text
            msg = bot.send_message(message.chat.id, "Please enter your age:")
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
            bot.register_next_step_handler(msg, process_gender_step)

    @bot.callback_query_handler(func=lambda call: call.data.startswith('gender_'))
    def process_gender_step(call):
        user_data['gender'] = call.data.split('_')[1]
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"Registration complete.\nUserName: {user_data['username']}\nName: {user_data['name']}\nAge: {user_data['age']}\nGender: {user_data['gender'].capitalize()}")
        # Remove the inline keyboard by editing the message and setting reply_markup to None
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        markup = types.InlineKeyboardMarkup()
        y_update = types.InlineKeyboardButton(text='Yes', callback_data='onfirm_yes')
        n_update = types.InlineKeyboardButton(text='No', callback_data='onfirm_no')
        markup.add(y_update, n_update)
        msg = bot.send_message(call.message.chat.id, "Do you confirm the data?:", reply_markup=markup)
        bot.register_next_step_handler(msg, process_confirmation)
        print (msg.text)
        
    
    @bot.callback_query_handler(func=lambda msg: msg.data.startswith('onfirm_'))
    def process_confirmation(msg):
        try:
            if msg.data == 'onfirm_yes':
                #bot.answer_callback_query(call.id, "Details confirmed.")
                bot.edit_message_reply_markup(chat_id=msg.message.chat.id, message_id=msg.message.message_id, reply_markup=None)
                bot.send_message(msg.message.chat.id, 'Thank you! Your details have been registered.')
                bot.edit_message_text(chat_id=msg.message.chat.id, message_id=msg.message.message_id, text='user ' + user_data['name'] + ' added!', reply_markup=None)
                sql.insert(msg.message.chat.id, user_data['username'], user_data['name'], user_data['age'], user_data['gender'])
            elif msg.data == 'onfirm_no':
                #bot.answer_callback_query(call.id, "Details not confirmed.")
                bot.edit_message_reply_markup(chat_id=msg.message.chat.id, message_id=msg.message.message_id, reply_markup=None)
                bot.edit_message_text(chat_id=msg.message.chat.id, message_id=msg.message.message_id, text='user ' + user_data['name'] + ' NOT added!', reply_markup=None)
                bot.send_message(msg.message.chat.id, "Registration cancelled. Use the command /alta to register")
        except:
            print ('error')

    @bot.message_handler(commands=['alta'])
    def send_alta(message):
        if sql.exists(message.chat.id):
            name = sql.exists(message.chat.id)
            bot.send_message(message.chat.id, name + ', you are already register. Use the command /borrar to delete your details from the system')
        else:
            ask_name(message)
