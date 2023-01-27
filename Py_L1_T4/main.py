"""
Напишите программу, которая
по заданному номеру четверти, показывает
диапазон возможных координат точек в этой четверти (x и y).
"""


def check(i):
    if i == 1:
        print("x > 0, y > 0")
    if i == 2:
        print("x < 0, y > 0")
    if i == 3:
        print("x < 0, y < 0:")
    if i == 4:
        print("x > 0, y < 0")


while True:
    print("введите номер четверти")
    x = int(input())
    if x < 1 or x > 4:
        print("Нет такой четверти")
    else:
        check(x)
        break
