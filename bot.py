from telebot import TeleBot
from telebot.types import Message

bot = TeleBot('7064462208:AAGxuOiK-gf8Z5mvQgQcIQ8-f9ZR2KZ0WiY')



@bot.message_handler(commands=['start', 'help'])
def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    print(chat_id)
    bot.send_message(chat_id, f"Assalomu alaykum {full_name}")


@bot.message_handler(content_types=["text", "photo"])
def get_text(message: Message):
    chat_id = message.chat.id
    text = message.text
    # bot.send_message(chat_id, text)
    bot.copy_message(-4184520416, chat_id, message.message_id)



bot.polling()