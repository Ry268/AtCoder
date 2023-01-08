t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    for j in range(n):
        if a[j] % 2 != 0:
            total += 1
    print(total)