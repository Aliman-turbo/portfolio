# a = int(input("Веди возраст"))
# while a >0:
#     print("С днём рождения")
#     a -=1
# class Cat:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# cat = Cat("Шарик",14)
# print(cat)


import random
rand_a_z = "qwertyuiopasdfghjklzxcvbnm!@#$%^&*/-+?~`=_12345678910"
rand_password_len = input("Введите длину пароля или check: ")
if rand_password_len == "check":
    length = int(input("Введите длину пароля для проверки сложности: "))
    if length < 8:
        print("Пароль слабый")
    elif 8 <= length <= 10:
        print("Пароль средний")
    elif length > 10:
        print("Пароль сильный")
else:
    rand_password = int(rand_password_len)
    ro = ""
    while len(ro) != rand_password:
        ro += random.choice(rand_a_z)
    print( ro)


def re():
    print("Регистрация")
    name = input("Введите своё имя:")
    pas = (input("Введите пароль Пароль дрожен быть не короче 5 символов и только латинскими буквами:"))
    if len(pas) < 6:
        print("Ошибка")
    return name,pas

name,pas = re()

def log(name,pas):
    p = input("Введите своё имя Для входа:")
    pasa = (input("Введите пароль для входа:"))

    if p != name and pasa != pas:
        print("Ошибка")

log(name,pas)
# import zipfile
# for i in range(5):
#     with open(f"Файл{i}.txt","w") as file:
#         file.write("text1")
# try:
#     with zipfile.ZipFile("cap_edu.zip","a",compression=zipfile.ZIP_DEFLATED, compresslevel=3) as myfile:
#         for i in range(5):
#             myfile.write(f"Файл{i}.txt")
#         print(myfile.namelist())
#         myfile.extractall("on_arch")
# except Exception:
#     print("Error")
# from turtle import *
# pensize(20)
# color("red")
# begin_fill()
# forward(100)
# left(120)
# forward(90)
# left(115)
# forward(90)
# end_fill()
# exitonclick()
# from turtle import *
# pensize(20)
# color("red")
# for i in range(5):
#     forward(100)
#     left(72)
# exitonclick()
# from turtle import *
# penup()
# goto(-350,0)
# pendown()
# for i in range(4):
#     left(90)
#     forward(100)
# penup()
# goto(-350,100)
# pendown()
# left(120)
# forward(90)
# left(115)
# forward(99)
# penup()
# goto(0,0)
# pendown()
# left(190)
# forward(90)
# right(150)
# forward(100)
# penup()
# goto(39,88)
# pendown()
# left(165)
# forward(100)
# right(220)
# forward(70)
# penup()
# goto(57,187)
# pendown()
# right(300)
# forward(80)
# penup()
# goto(36,198)
# pendown()
# circle(30)
# exitonclick()

