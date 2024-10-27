import telebot
import cfg

bot = telebot.TeleBot(cfg.TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ПРИВ ЛОЛ")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_photo(message.chat.id, "help")

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Информация о боте:')

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])

@bot.message_handler(func=lambda message: True)
def check_message(message):
    if "https://" in message.text:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Ссылки запрещены!')
    else:
        pass

bot.infinity_polling()