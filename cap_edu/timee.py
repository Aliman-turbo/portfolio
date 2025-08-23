# import time
# now_time = 11
#
# while now_time != 1:
#     now_time = now_time - 1
#     print(now_time)
#     if now_time == 1:
#         print("Таймер завершился")
#Задание 2
# from time import *
# stop_time = input("Введи 1 для начала таймера и 0 для оканчани секундамера")
# while stop_time != "0":
#     if stop_time == "1":
#         start = time()
#     else:
#         print("A")
#     stop_time = input("Введи 1 для начала таймера и 0 для оканчания секундомера")
# end = time()
# time = end - start
# print("Окончвние времени ", round(end))


# import re
# pattern = r'\w+@\w+\.\w+'
# my_email = 'Почта alimoldogaliev776@gmail.com'
# match = re.findall(pattern,my_email)
# print(match)
#
# pattern1 = r'\d{3}-\d{3}-\d{4}'
# my_email1 = 'Номера телефонов 111-222-5555 , 888-145-8585 , 456-414-1234'
# match1 = re.findall(pattern1,my_email1)
# print(match1)
#
# pattern2 = r'\d{2}\.\d{2}\.\d{4}'
# my_email2 = 'Дни 15.10.2025'
# match2 = re.sub(pattern2,'2025.10.15',my_email2)
# print(match2)


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"Меня зовут {self.name} а мой возраст {self.age}")
#     def rop(self):
#         self.age += 1
# asd = Person("Али",12)
# sa = Person("Науан",15)
# asd.rop()
# asd.introduce()
# sa.rop()
# sa.introduce()

class Client:
    def __init__(self,client_id,name,balance = 0):
        self.client_id = client_id
        self.name = name
        self.balance = balance
    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Баланс пополнен на счёт {amount} текущий баланс {self.balance}")
        else:
            print("Сумма пополнения должна быть больше 0 тенге")
    def withdraw(self,amount):
        if amount > self.balance:
            print(f"Недостаточно средств Баланс{self.balance}")
        else:
            self.balance -= amount
            print(f"Снято {amount} текущий баланс {self.balance}")
    def showbalance(self):
        print(f"Текущий баланс{self.balance}")
class ATM:
    def __init__(self):
        self.clients = {}
    def add_client(self,client):
        self.clients[client.client_id] = client


