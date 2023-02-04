n = int(input())
numb = []
for _ in range(n):
    numb.append(int(input()))
x = int(input())
max = numb[0]
min = numb[0]
temp = 0
for i in numb:
    if i >= max:
        temp = max
        max = i
        i = temp
    if i <= min:
        temp = min
        min = i
        i = min
if x > max:
    print(max)
elif x < min:
    print(min)
else:
    print(x)
