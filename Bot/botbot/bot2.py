import json
import json as pg
import random
import telebot
from telebot import types
from datetime import date,timedelta
# импорты библиотек
TOKEN ="7635903004:AAGbwRMFIE_afG16mJnzeBlxndWBqSLs-dw"


bot = telebot.TeleBot(TOKEN)
# токен бота


@bot.message_handler(commands=["start"])# команда старт
def handle_start(message):# функция стврт
    bot.send_message(message.chat.id, "Бот для записи на процедуры запущен")# вывод сообщения что бот запущен
    # keydoard = generate_button()# генерация кнопки
    # bot.send_message(message.chat.id,"Выбери настроение:",reply_markup=keydoard)# выбор кнопки


@bot.message_handler(commands=["show_dates"])
def handle_schedule(message):
    keyboard = handle_show_dates()
    bot.send_message(message.chat.id,"Выберите день",reply_markup=keyboard)



def handle_show_dates():

    keyboard = types.InlineKeyboardMarkup()
    days =[]
    for i in range(7):
        days.append(date.today()+timedelta(days=3+i))
    for button in days:
        callback_data =f"day:{button}"
        b = types.InlineKeyboardButton(text=button,callback_data=callback_data)
        keyboard.add(b)
    return keyboard
def generate_keyboard(date):
    keyboard = types.InlineKeyboardMarkup()
    times = ["10:00", "12:00", "15:00", "17:00"]
    with open("data.json" ,"r",encoding="utf-8") as f:
        f = json.load(f)
        for i in f["appointments"]:
            if i["date"] == date:
                times.remove(i["time"])

    for i in times:
        callback_data = f"meeting: {i}"
        btn = types.InlineKeyboardButton(text=i,callback_data=callback_data)
        keyboard.add(btn)
    return keyboard





@bot.callback_query_handler(func=lambda call : True)# функция которая вызываеться только 1 раз но так как это бессконечность он будет вызван всегда
def handle_button_click(call):# функция проверки на то что человек нажал на кнопку
    if call.data.startswith("day:"):
        f = call.data.split(":")[1]
        bot.send_message(call.message.chat.id,f"Вы выбрали дату:{f}")
        bot.send_message(call.message.chat.id,"Выберите время",reply_markup=generate_keyboard())
    elif call.data.startswith("appointments:"):
        f,chousen_time = call.data.split(":")[1], call.data.split(":")[2]
        add_appointments(f,chousen_time,call.message.chat.id)
        bot.send_message(call.message.chat.id,f'ВЫ ЗАПИСАНЫ НА {f}  И В {chousen_time}')
def add_appointments(date,time,client):
    try:
        with open("data.json","r",encoding="utf-8") as js:
            json_js = json.load(js)
    except FileNotFoundError:
        json_js = {"appointments":[],"review":[]}
    new_appointment = {"date":date,"time":time,"client":client}
    json_js["appointments"].append(new_appointment)
    with open("data.json", "w", encoding="utf-8") as js:
        json.dump(json_js,js)











if __name__ == "__main__":# чтобы бот запустился
    bot.polling(none_stop=True)
