"""
Задача 4: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
не превосходящие числа N.
Пример 10: 1, 2, 3
"""
i = 1
a = 10
while i <= a:
    if i < a:
        if i * 2 > a:
            break
        else:
            i = i * 2
            print(i)
