import telebot
import time

current_time = time.time()
formatted_time = time.ctime(current_time)

token = "7894788565:AAFURkRRGW0C0tsiU75OcSLesWJEQwa9wYQ"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,"ПРивет это бот который бкдет тебе напоминеать пить воду!\n"
                                     "Есть функция /time которая выводит время\n"
                                     "Есть функция /setreminder1 которая засикает 1 час\n"
                                     "Есть функция /drink которая показывает сколько тебе осталось выпить ")
@bot.message_handler(commands=["time"])
def now_time(message):
    bot.send_message(message.chat.id,f"Сейчас: {formatted_time}")
@bot.message_handler(commands=["setreminder1"])
def start_time(message):
    bot.send_message(message.chat.id,f"Время пошло!")
    time.sleep(3600)
    bot.send_message(message.chat.id, f"Выпей стакан воды время вышло!")
@bot.message_handler(commands=["drink"])
def now_time(message):
    bot.send_message(message.chat.id,"После этого сообщения напиши сколько мл воды выпел")
    bot.register_next_step_handler(message,get_water_message)
def get_water_message(message):
    water = 3000
    water_user = int(message.text)
    bot.send_message(message.chat.id,f" Ты выпил {water_user} Тебе осталось выпить {water-water_user}")


if __name__ == "__main__":
    bot.polling()