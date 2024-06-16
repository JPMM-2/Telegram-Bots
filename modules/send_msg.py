# main.py
import telebot

from config import *


# Replace 'YOUR_BOT_TOKEN' with the token you got from BotFather
BOT_TOKEN = 'YOUR_BOT_TOKEN'
USER_ID = 6573427258  # Replace with the actual user ID
MESSAGE = 'Hello! This is a testjhfyhyfjyhgt message.'

# Initialize the bot
API_TOKEN = 'YOUR_API_TOKEN'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Function to send a message
def send_message(user_id, message):
    try:
        bot.send_message(user_id, message)
        print(f'Message sent to user {user_id}')
    except Exception as e:
        print(f'Failed to send message: {e}')

# Send the message
send_message(USER_ID, MESSAGE)
