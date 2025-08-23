
from telebot import types
import telebot
token = "7349545982:AAGrP0pykrsQSrSZd4xgqN-6Q4zesyB7bTo"
bot = telebot.TeleBot(token)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttom1 = types.KeyboardButton("Кнопка 1")
buttom2 = types.KeyboardButton("Кнопка 2")
markup.add(buttom1)
markup.add(buttom2)
@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,("start do"))
@bot.message_handler(commands=["help"])
def help_message(message):
    bot.send_message(message.chat.id,"Команды\n 1 /button выход кнопки \n 2 /start Старт \n 3 /smile")
@bot.message_handler(commands=["smile"])
def start_message(message):
    bot.send_message(message.chat.id, ("😎"))
@bot.message_handler(commands=["button"])
def button1(message):
    bot.send_message(message.chat.id,"Это кнопка ",reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Кнопка 1":
        bot.send_message(message.chat.id,"ВЫ нажали на кнопку 1 ")
    elif message.text == "Кнопка 2":
        bot.send_message(message.chat.id, "Школа Cap", reply_markup=markup)

bot.infinity_polling()