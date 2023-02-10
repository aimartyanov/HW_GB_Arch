n = int(input())
a = list(map(int, input().split()))
x = 0
i = 1
for i in range(1, n-1):
    if a[i]+a[i + 1]+a[i - 1] > x:
        x = a[i]+a[i+1]+a[i-1]
print(x)
