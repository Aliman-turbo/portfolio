import telebot
import browzer

# Замените 'ВАШ_ТОКЕН' на токен, полученный от BotFather
TOKEN = "7747467374:AAFQkxwV_lsvsw6fZwYhmscIn-8Gj8_joRs"
bot = telebot.TeleBot(TOKEN)


# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Добро пожаловать в справочный бот по фильмам!")


@bot.message_handler(func=lambda message: True)
def response(message):
    ds = message.text
    movie_url = browzer.get_movie_url(ds)
    if movie_url:
        sop = browzer.get_movie_info(movie_url)
        if sop:
            text = f"Название:{sop["title"]},Описание:{sop["description"]}"
            bot.send_message(message.chat.id,text)
        else:
            bot.send_message(message.chat.id,"Ошибка")
    else:
        bot.send_message(message.chat.id, "Ошибка")
bot.polling()