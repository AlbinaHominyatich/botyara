import telebot
bot = telebot.TeleBot("6213672829:AAEjT_brCjdI4V7Rs3Ue174A3e6GQUXi8LI")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello🙊')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, "Усі кажуть " + message.text + " ,а ти купи слона")
bot.polling()
