"""
Задача 4: Требуется определить, можно ли от шоколадки размером n × m
долек отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два прямоугольника).
3 2 4 -> yes
3 2 1 -> no
"""
n = int(input())
m = int(input())
k = int(input())


def chockolate(n, m, k):
    if ((k % n == 0) or (k % m == 0)) and (k < n * m):
        print("yes")
    else:
        print("no")


chockolate(n, m, k)