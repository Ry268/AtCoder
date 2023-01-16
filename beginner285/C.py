S = input()

hashmap = {}
count = 1

for i in range(65, 91):
    hashmap[chr(i)] = count
    count += 1

i = 0    
total = 0    
    
for char in S[::-1]:
    if i == 0:
        total += hashmap[char]
    else:
        total += hashmap[char] * 26 ** i
    i += 1
print(total)