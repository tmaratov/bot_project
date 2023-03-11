import telebot

token = '5979685133:AAE1ciAqk800SNOsjtd91udbVdzFeQjWtz4'

bot = telebot.TeleBot(token)




@bot.message_handler(commands=['start'])
def welcome_message(message):
    welcome_message = 'Работает?'
    bot.send_message(message.chat.id, welcome_message)






bot.infinity_polling()