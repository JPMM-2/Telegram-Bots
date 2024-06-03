
from telebot import types
import options

def handle_saludar(bot):
    
	@bot.message_handler(commands=['start'])
	def send_saludarr(message):	
		bot.send_message(message.chat.id, 'hello')
		bot.send_message(message.chat.id, 'welcome ')        
		markup = types.InlineKeyboardMarkup()
		btn_servicios = types.InlineKeyboardButton(text='Servicios', callback_data='saludo_servicios')
		btn_facebook = types.InlineKeyboardButton(text='Facebook', callback_data='saludo_facebook')
		btn_cita = types.InlineKeyboardButton(text='Pedir cita', callback_data='saludo_cita')
		markup.add(btn_servicios, btn_facebook, btn_cita)
		msg = bot.send_message(message.chat.id, "How I can help you??", reply_markup=markup)

	options.handle_options(bot)
