def solve(n:int, numArrays:list) -> int:
    count = 0
    for i in range(n):
        if numArrays[i] % 2 != 0:
            count += 1
    return count

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = solve(n, a)
    print(total)