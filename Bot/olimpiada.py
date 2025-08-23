# import math
# def dist(x1,y1,x2,y2):
#     return math.sqrt((x2 - x1)**2+(y2 - y1)**2)
# def naklon(x1,y1,x2,y2,x3,y3,x4,y4):
#     return (y2 - y1)/(x2 - x1) == (y4 -y3)/(x4-x3)
# def otvet(points):
#     x1, y1, x2, y2, x3, y3, x4, y4 = points
#     if (naklon(x1,y1,x2,y2,x3,y3,x4,y4) and naklon(x1,y1,x4,y4,x2,y2,x3,y3) and dist(x1,y1,x2,y2)== dist(x3,y3,x4,y4) and dist(x1, y1,x4,y4)== dist(x2,y2,x3,y3)) :
#         print("Yes")
#     else:
#         print("No")
# n = int(input())
# results = []
#
# for _ in range(n):
#     points = list(map(int, input().split()))
#     results.append(otvet(points))
# for result in results:
#     print(result)


# def s(correct,not_correct):
#     k = next(i for i in range(len(correct)) if correct[i]!= not_correct[i])
#     series = correct[:k]
#     posibble = set()
#     correct_ost = correct[k:]
#     not_correct_ost = not_correct[k:]
#
# d = ["a","a","g"]
# h = set(d)
# print(h)
# while True:
#     a = int(input("число 1"))
#     b = int(input("число 2"))
#     v = a+b
#     print(v)
#     s = input("Надо ли заверщить програму")
#     if s == "Y"or s == "y":
#         break
# N = int(input("Введи число факториал"))
# d = 1
# for i in range(1,N+1):
#     d = (d*i)
# print(d)
# a = 0
# for i in range(1,5050+1):
#     a = a +1
# print(a)
# N = int(input("Введи число"))
# for i in range(1,N):
#     if :
#         N = N + 1
# #         print(N)
#
#
# def cheb(cheb_tic,brok_tic):
#     Ansi = [chr(i) for i in range(256)]
#     dlina_serii = len(cheb_tic.split()[0])
#     vozmo_tic = set()
#     def generate_comb(current,index):
#         if index == len(brok_tic):
#             if current[:dlina_serii] == cheb_tic[:dlina_serii]:
#                 vozmo_tic.add(current)
#             return
#         if brok_tic[index] == "?":
#             for char in Ansi:
#                 generate_comb(current +char,index + 1)
#         else:
#             generate_comb(current + brok_tic[index],index + 1)
#     generate_comb("",0)
#     return sorted(vozmo_tic)
#
# results = cheb("654607199323","cSCc♥s!!Y?Z#3")
# print("\n".join(results))



# def generate_combinations(current,index):
#     if index == len(broken_ticket):
#         if current[:prefix_lenght]
a = ["Али","Нау","ig"]
b = [1,2]
b.sort(reverse=True)
print(b)







# def d(x,y):
#     if abs(x - y) > 1 and min(x,y) == 0:
#         return "No SOLUTION "
#     result = ""
#     if x > y :
#         result = "bg" * y + "b"
#     elif x < y:
#         result = "gb" * x + "g"
#     else:
#         result = "bg" * x
#     return result
# x, y = map(int, input().split())
# print(d(x,y))

# a = int(input("Число 1"))
# b = int(input("Число 2"))
# if a > b:
#     print(f"{a} это число больше")
# else:
#     print(f"{b} это число больше")
# a = int(input("Введи число1:"))
# b = int(input("Введи число2:"))


# def n(N,i,j):
#     direct_road = abs(j - i) - 1
#     obratnui_road = N - abs(j-i) - 1
#     return min(direct_road,obratnui_road)
# N, i, j = map(int, input("Введите N, i и j через пробел: ").split())
# print(n(N,i,j))
#












#Всего 2 пути: 1 путь: прямой путь от станции i до станции j и 2 путь: путь в обратном направлении(по кольцу) от станцииiдостанцииj
# def n(N,i,j):
#     #ОПРЕДЕЛЯЕМ ПРЯМОЙ ПУТЬ
#     direct_road = abs(j-i) - 1
#     #здесь мы вычесляем кол во промежуточных станции
#     #если Болат поедет по прямому пути от станции i к станции j ю для этого мы вычесляем растояние в стациях между i т j, функция абс используеться чтобы получить положительные значения не зависимо от того больше  i чем j или наоборотю поскольку нас интересует кол во промежуточных ствнции мы вычитаем 1 иначе посчиттаеться и конечная ствнция j
#     obratnui_road = N - abs(j-i) - 1
#     return min(direct_road,obratnui_road)
# N, i, j = map(int, input("Введите N, i и j через пробел: ").split())
# print(n(N,i,j))