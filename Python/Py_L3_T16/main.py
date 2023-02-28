n = int(input())
numb = []
i = 0
for _ in range(n):
    numb.append(int(input()))
x = int(input())
for a in numb:
    if x == a:
        i = i+1
print(i)
