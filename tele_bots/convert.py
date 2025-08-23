
import telebot
import requests
from  telebot import types
token = "7889025492:AAEGs4MccM_E35ufDJlRFlPHRvSeaYU2Dds"
API = "7e8730391483f1ba10a43730"
bot = telebot.TeleBot(token)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("USD TO KZT")
button2 = types.KeyboardButton("KZT TO USD")
markup.add(button1, button2)
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
                print(f"❗Валюта {target_currency} не найдена в ответе.")
                return None
        else:
            print(f"❗Ошибка запроса: статус {response.status_code}")
            return None
    except Exception as e:
        print(f"❗Ошибка соединения: {e}")
    return None
@bot.message_handler(commands=['convert'])
def convert_curancy(message):
    try:
        _, amount,base_currency,target_currency = message.text.split()
        amount = float(amount)

        

        exhange_rate = get_exhange_rate(base_currency.upper(),target_currency.upper())
        converted_amount = float(amount *exhange_rate)

        if exhange_rate:
            bot.send_message(message.chat.id,f"{amount}{base_currency.upper()} is {converted_amount}{target_currency.upper()}")
        else:
            bot.reply_to(message,"error")
    except ValueError:
        bot.reply_to(message,"Введите сумму")
    except Exception as e:
        bot.reply_to(message,e)
@bot.message_handler(commands=["help"])
def help_fun(message):
    bot.send_message(message.chat.id,"Есть /button которая аоказывает кнопки и можнор написать сначала сумму потом выбрать формат USD KZT илм KZT USD 1 вариант переводит из долларов в тенге второй из тенге в деллары!!!")

@bot.message_handler(commands=["button"])
def button_message(message):
    bot.send_message(message.chat.id,"Кнопки для Конвертации",reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "USD TO KZT":
        bot.send_message(message.chat.id, "Напишите сумму в долларах:")
        bot.register_next_step_handler(message, get_text)
    elif message.text == "KZT TO USD":
        bot.send_message(message.chat.id, "Напишите сумму в тенге:")
        bot.register_next_step_handler(message, get_text2)
def get_text(message):

    amount = float(message.text)
    exchange_rate = get_exhange_rate("USD", "KZT")
    if exchange_rate:
        converted_amount = amount * exchange_rate
        bot.send_message(message.chat.id, f"{amount} долларов в {converted_amount:.1f} тенге")
    else:
        bot.send_message(message.chat.id, "Ошибка")


def get_text2(message):
    amount = float(message.text)
    exchange_rate = get_exhange_rate("KZT", "USD")
    if exchange_rate:
        converted_amount = amount * exchange_rate
        bot.send_message(message.chat.id, f"{amount} тенге в {converted_amount:.1f} долларах")
    else:
        bot.send_message(message.chat.id, "Ошибка")
if __name__ == "__main__":
    bot.polling()