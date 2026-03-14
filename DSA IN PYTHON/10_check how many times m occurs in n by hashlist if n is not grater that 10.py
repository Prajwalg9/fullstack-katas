from random import randint

n = [randint(1,10) for i in range(1,31)]
m = [randint(1,30) for i in range(1,31)]
hashlist = [0]*11
hashdict= dict()

print(n)
print(m)

for num in n:
    hashlist[num] += 1

for num in m:
    if num<0 or num>10:
        hashdict[num] =0
    else:
        hashdict[num] = hashlist[num]

print(hashdict)

