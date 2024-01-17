import sys
n = int(input())
oiler = [i for i in range(n + 1)]
prime_num = []
for i in range(2,n + 1):
    prime = True
    for j in range(2,int(i**0.5 + 1)):
        if i % j == 0:
            prime = False
            break
    if prime:
        prime_num.append(i)

for i in prime_num:
    if i == oiler[i]:
        for j in range(i,n + 1,i):
            oiler[j] = oiler[j] - (oiler[j]//i)

print(oiler[n])
