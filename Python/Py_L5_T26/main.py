def power(base, exp):
    if exp == 1:
        return base
    if exp != 1:
        return base * power(base, exp - 1)


print("Введите число: ")
base = int(input())
print("Введите его степень: ")
exp = int(input())
print(power(base, exp))
