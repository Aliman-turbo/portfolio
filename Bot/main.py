import json as pg
import random

import telebot

TOKEN = "7041875080:AAFxG6C01HycWpfrFLqd6Id_8yD2ekJb974"

with open("user_data.json","r",encoding="utf-8") as f:
    user_data = pg.load(f)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет я бот")



@bot.message_handler(commands=["learn"])
def handle_learn(message):

    user_words = user_data.get(str(message.chat.id),{})
    try:
        words_number = int(message.text.split()[1])
        ask_translation(message.chat.id,user_words,words_number)
    except ValueError:
        bot.send_message(message.chat.id,"ошибка число введено не правильно, введите команду /learn количество  ")
    except IndexError:
        bot.send_message(message.chat.id,"ошибка у вас не достаточно записаных слов ")





@bot.message_handler(commands=["addword"])
def handle_addword(message):
    global user_data
    chat_id = message.chat.id
    user_dict = user_data.get(chat_id,{})
    words = message.text.split()[1:]
    try:
            if len(words) == 2:
                words,translation = words[0].lower(),words[1].lower()
                user_dict[words] = translation
                user_data[chat_id] = user_dict
                with open("user_data.json","w",encoding="utf-8") as f:
                    pg.dump(user_data,f,ensure_ascii=False,indent=4)
                    bot.send_message(chat_id,f"Слово {words} добавлено в словарь.")
            else:
                bot.send_message(chat_id, "Произошла ошибка попробуйте ещё раз")
    except Exception:
        print("Ошибка")

def ask_translation(chat_id,user_words,words_left):
    if words_left > 0:
        word = random.choice(list(user_words.keys()))
        translation = user_words[word]
        bot.send_message(chat_id,f"Напиши перевод слова {word}.")
        bot.register_next_step_handler_by_chat_id(chat_id,chek_translation,translation,words_left)

def chek_translation(message,expected_translation,words_left):
    user_translation = message.text.strip().lower()
    if user_translation == expected_translation:
        bot.send_message(message.chat.id,"Правильно")
    else:
        bot.send_message(message.chat.id, f"Правильный перевод {expected_translation}")
    ask_translation(message.chat.id,user_data[str(message.chat.id)],words_left-1)
    



@bot.message_handler(func=lambda message:True)
def handle_all(message):
    if message.text.lower() == "как тебя зовут ?":
        bot.send_message(message.chat.id,"Меня зовут Али" )
    elif message.text.lower() == "сколько тебе лет ?":
        bot.send_message(message.chat.id, "Мне 8 лет")
    elif message.text.lower() == "расскажи шутку ?":
        bot.send_message(message.chat.id, "я не умею рассказывать шутки")
    elif message.text.lower() == "как дела?":
        bot.send_message(message.chat.id, "нормально")


if __name__ == "__main__":
    bot.polling(none_stop=True)


























# import pygame
#
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Моя игра")
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     pygame.display.flip()
#
# pygame.quit()
#
# background = pygame.image.load("station-8558516_1280.webp.png")
# #sprite = pygame.image.load("sprite.png")


