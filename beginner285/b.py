N = int(input())
S = input()

for i in range(N-1):
    count = 0
    for j in range(i+1, N):
        if S[count] == S[j]:
            break
        else:
            count += 1
    print(count)