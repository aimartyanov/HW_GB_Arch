def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum(a-1, b+1)


print("Введите число: ")
a = int(input())
print("Введите число: ")
b = int(input())
print(sum(a, b))
