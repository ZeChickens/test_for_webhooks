from telebot import TeleBot

bot = TeleBot("767498673:AAHBW_5Vw1Qk0DNef9T4QWLd2VV4YXB3eN4")

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(chat_id=message.chat.id, text="LOL")

bot.polling()