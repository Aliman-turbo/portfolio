import telebot
import requests
from  telebot import types
token = "7889025492:AAEGs4MccM_E35ufDJlRFlPHRvSeaYU2Dds"
API = "7e8730391483f1ba10a43730"
bot = telebot.TeleBot(token)
curencies = ["USD","EUR","KZT","RUR","CNY","BYN","BRL","CAD","ZAR"]
user_data = {}
def get_exhange_rate(base_currency, target_currency):
    url = f'https://v6.exchangerate-api.com/v6/{API}/latest/{base_currency}'
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            rates = data.get('conversion_rates', {})
            rate = rates.get(target_currency)
            if rate:
                return rate
            else:
                val_error = f"❗Валюта {target_currency} не найдена в ответе."
                print(val_error)
                return None
        else:
            zap_error=  f"❗Ошибка запроса: статус {response.status_code}"
            print(zap_error)
            return None
    except Exception as e:
        enter_error = f"❗Ошибка соединения: {e}"
        print(enter_error)
    return None
@bot.message_handler(commands=["curs"])
def get_rate(message):
    bot.send_message(message.chat.id, "Введите валюту из которой хотите узнать:")
    bot.register_next_step_handler(message, curs_base_currency)
def curs_base_currency(message):
    base_currency = message.text.upper()
    if base_currency in curencies:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for currency in curencies:
            markup.add(currency)
        bot.send_message(message.chat.id, "Выберите валюту к которой хотите перевесмти:", reply_markup=markup)
        bot.register_next_step_handler(message, curs_target_currency, base_currency)
    else:
        bot.reply_to(message, "Такойц валюты нет")

def curs_target_currency(message, base_currency):
    target_currency = message.text.upper()
    if target_currency in curencies:
        exchange_rate = get_exhange_rate(base_currency, target_currency)
        if exchange_rate:
            bot.send_message(message.chat.id, f"Курс {base_currency} к {target_currency}: {exchange_rate}")
        else:
            bot.send_message(message.chat.id, "Запрос некоректенн")
    else:
        bot.reply_to(message, "Попробуйте снова.")

@bot.message_handler(commands=["start","help"])
def welcome (message):
    bot.reply_to(message,'Добро пожаловать в наш бот! вызови команду /convert потом введи сумму потом выбери валюты')
@bot.message_handler(commands=["convert"])
def start_convertion(message):
    user_data[message.chat.id] = {}
    sum_convert_l = "Введите вам нужную сумму денеег для конвертации:"
    bot.send_message(message.chat.id,sum_convert_l)
    bot.register_next_step_handler(message, English)
    bot.register_next_step_handler(message,process_amount)
def process_amount(message):
    try:

        amount = float(message.text)
        user_data[message.chat.id]["amount"] = amount
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for curency in curencies:
            markup.add(curency)
        choose_val = "Выберите одну из валют ниже:"
        bot.send_message(message.chat.id,choose_val,reply_markup=markup)
        bot.register_next_step_handler(message, English)
        bot.register_next_step_handler(message,process_base_curency)
    except ValueError:
        n_l = "Введите число!"
        bot.reply_to(message,n_l)
def process_base_curency(message):
    base_curency = message.text.upper()
    if base_curency in curencies:
        user_data[message.chat.id]["base_currency"]=base_curency
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for curency in curencies:
            markup.add(curency)
        per_money = "Выберите валюты в которые вы хотите перевести деньги"
        bot.send_message(message.chat.id,per_money)
        bot.register_next_step_handler(message,English)
        bot.register_next_step_handler(message,process_target_currency)
def process_target_currency(message):
    target_currency = message.text.upper()
    if target_currency in curencies:
        user_data[message.chat.id]["target_currency"] = target_currency
        amount = user_data[message.chat.id]["amount"]
        base_curency = user_data[message.chat.id]["base_currency"]
        exchange_rate = get_exhange_rate(base_curency,target_currency)
        if exchange_rate:
            converted_amount = amount*exchange_rate
            bot.send_message(message.chat.id,f"{amount} {base_curency} в {converted_amount} {target_currency}")
        else:
            bot.send_message(message.chat.id,"error")
    else:
        bot.reply_to(message,"error")
def English(message):
    if message == "English":
        bot.send_message(message.chat.id,"Перевод на Английский")
@bot.message_handler(func=lambda message:True)
def eho_all(message):
    bot.reply_to(message,"Неизвестная  команда")
if __name__ == "__main__":
    bot.polling()


        



