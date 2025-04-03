import telebot
TOKEN = '7628929979:AAF5r53k2Rrtkp8cvNOcXaLQq5S0NR5bJfU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def start_command(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
