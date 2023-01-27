"""
Напишите программу для. проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""


def check(x, y, z):
    left = not (x or y or z)
    right = not x and not y and not z
    result = left == right
    return result


print("Введите x")
x = int(input())
print("Введите y")
y = int(input())
print("Введите z")
z = int(input())


if check(x, y, z):
    print("Утверждение истинно")
else:
    print("Утверждение ложно")
