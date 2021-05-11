import telebot
bot = telebot.TeleBot('1715318435:AAEjzF9z0XlNwuL2MAwYyqxcpv6pGn6hsBQ')
@bot.message_handler(commands = ['start','help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет, я бот-повторюшка. Напиши мне что-нибудь.')

@bot.message_handler(func = lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()