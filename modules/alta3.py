
# module_alta.py
from telebot import types
import sqlite as sql
import functions

def handle_alta(bot):
    user_data = {}

    def ask_name(message):
        user_data['username'] = message.from_user.first_name
        msg = bot.send_message(message.chat.id, "Please enter your name:")
        bot.register_next_step_handler(msg, process_name_step)

    def process_name_step(message):
        try:
            user_data['name'] = message.text
            msg = bot.send_message(message.chat.id, "Please enter your number:")
            bot.register_next_step_handler(msg, process_number_step)
        except Exception as e:
            bot.send_message(message.chat.id, 'Something went wrong. Please try again.')    

    def process_number_step(message):
        try:
            t_num = functions.t_number(message.text)
            if t_num == 'ok':
                user_data['number'] = message.text
                msg = bot.send_message(message.chat.id, "Please enter your age:")
                bot.register_next_step_handler(msg, process_age_step)
            else:
                msg = bot.send_message(message.chat.id, t_num)
                bot.register_next_step_handler(msg, process_number_step)
        except Exception as e:
            bot.send_message(message.chat.id, 'Something went wrong. Please try again.')

    def process_age_step(message):
        try:
            age_msg = functions.edad(message.text)
            if age_msg == 'ok':
                user_data['age'] = message.text
                markup = types.InlineKeyboardMarkup()
                btn_male = types.InlineKeyboardButton(text='Male', callback_data='gender_male')
                btn_female = types.InlineKeyboardButton(text='Female', callback_data='gender_female')
                btn_other = types.InlineKeyboardButton(text='Other', callback_data='gender_other')
                markup.add(btn_male)
                markup.add(btn_female)
                markup.add(btn_other)
                bot.send_message(message.chat.id, "Please select your gender:", reply_markup=markup)
            else:
                msg = bot.send_message(message.chat.id, age_msg)
                bot.register_next_step_handler(msg, process_age_step)
        except ValueError:
            msg = bot.send_message(message.chat.id, "Invalid age. Please enter a number between 18 and 130:")
            bot.register_next_step_handler(msg, process_age_step)

    @bot.callback_query_handler(func=lambda call: call.data.startswith('gender_'))
    def process_gender_step(call):
        user_data['gender'] = call.data.split('_')[1]
        bot.answer_callback_query(call.id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        bot.send_message(call.message.chat.id, f"Registration complete.\nUserName: {user_data['username']}\nName: {user_data['name']}\nAge: {user_data['age']}\nGender: {user_data['gender'].capitalize()}")

        markup = types.InlineKeyboardMarkup()
        btn_yes = types.InlineKeyboardButton(text='Yes', callback_data='confirm_yes')
        btn_no = types.InlineKeyboardButton(text='No', callback_data='confirm_no')
        markup.add(btn_yes, btn_no)
        bot.send_message(call.message.chat.id, "Do you confirm the data?", reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: call.data.startswith('confirm_'))
    def process_confirmation(call):
        try:
            if call.data == 'confirm_yes':
                bot.answer_callback_query(call.id, "Details confirmed.")
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
                sql.insert(call.message.chat.id, user_data['username'], user_data['name'], user_data['number'], user_data['age'], user_data['gender'])
                bot.send_message(call.message.chat.id, 'Thank you! Your details have been registered.')
            elif call.data == 'confirm_no':
                bot.answer_callback_query(call.id, "Details not confirmed.")
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
                bot.send_message(call.message.chat.id, "Registration cancelled. Use the command /alta to register again.")
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    @bot.message_handler(commands=['alta'])
    def send_alta(message):
        if sql.exists(message.chat.id):
            name = sql.exists(message.chat.id)
            bot.send_message(message.chat.id, f"{name}, you are already registered. Use the command /borrar to delete your details from the system.")
        else:
            try:
                ask_name(message)
            except:
                print ('error alta')
                pass
