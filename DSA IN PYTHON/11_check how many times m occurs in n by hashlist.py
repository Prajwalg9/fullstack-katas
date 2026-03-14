from random import randint

n = [randint(1,100) for i in range(1,31)]
m = [randint(1,100) for y in range(1,31)]
print(n)
print(m)
hashdict = {}
frequency_map=dict()

for num in n:
    if num in hashdict:
        hashdict[num] += 1
    else:
        hashdict[num] = 1

for num in m:
    if num in hashdict:
        frequency_map[num] =hashdict[num]
    else:
        frequency_map[num] = 0

print(frequency_map)