import datetime
# class Field:
#     def __init__(self, size, ships):
#         self.size = size
#
#         self.ships_alive = ships
#         self.grid = []
#         for _ in range(size):
#             self.grid.append([None] * size)
#
#     def display(self, show_ships=False):
#         self.show_ships = show_ships
#
#         # вывод строки с буквами
#
#         for i, row in enumerate(self.grid):
#             display_row = ""
#             for cell in row:
#                 # проверка, что ячейка пустая
#                 display_row += "O "
#             else:
#                 display_row += "■ "
#             if i + 1 != 10:  # вывод ноликов и квадратиков
#                 print(i + 1, "0 ", display_row)
#             else:
#                 print(i + 1, "■", display_row)
vrema = datetime.date.today()
r_vrema = datetime.date(2024,11,6)
tree_time = vrema - r_vrema
print(tree_time)