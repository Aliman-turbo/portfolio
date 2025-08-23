

import telebot
import requests
from telebot import types

token = "8192482729:AAEnGjsNbpNgczQPhdu-S43brhaRFtr30lQ"
weather_API = "327db86450744bb2a2a115508252505"
bot = telebot.TeleBot(token)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Astana")
button2 = types.KeyboardButton("Moscow")
markup.add(button1, button2)


def get_weather(city):
    try:
        url = f"https://api.weatherapi.com/v1/current.json?key={weather_API}&q={city}&aqi=no"
        response = requests.get(url)
        data = response.json()

        if "error" not  in data:
            current = data["current"]
            location = data["location"]["name"]
            country = data["location"]["country"]
            weather_temp = current["temp_c"]
            weather_desc = current["condition"]["text"]
            weather_speed = current["wind_kph"]
            humidity = current["humidity"]

            weather_report = (
                f"Погода сейчас в: {location}, {country}\n"
                f"Температура: {weather_temp}C\n"
                f"Скорость ветра: {weather_speed} км/ч\n"
                f"Описание: {weather_desc}\n"
                f"Влажность: {humidity}%\n"
            )
        else:
            weather_report = "Ошибка в названии города"

    except:
        weather_report = "Ошибка при получении данных"

    return weather_report


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Здравствуйте бот для прогноза погоды.", reply_markup=markup)


@bot.message_handler(commands=["button"])
def button_message(message):
    bot.send_message(message.chat.id, "Выберите город:", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    city = message.text.strip()

    if city in ["Astana", "Moscow"]:
        weather_report = get_weather(city)
        bot.send_message(message.chat.id, f"Сейчас в {city}:\n{weather_report}")
    else:
        bot.send_message(message.chat.id, "Введите корректное название города")


bot.polling()

