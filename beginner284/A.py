n = int(input())
s = [None] * n

for i in range(n):
    s[i] = input()

for i in range(n - 1, -1, -1):
    print(s[i])