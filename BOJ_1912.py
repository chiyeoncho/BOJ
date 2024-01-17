import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
sumN = []
sumN.append(num[0])
answer = sumN[0]
minN = 0

for x in range(1,n):
    sumN.append(sumN[x - 1] + num[x])
    if sumN[x] - minN > answer:
        answer = sumN[x] - minN
    if num[x] > answer:
        answer = num[x]
    if sumN[x] < minN:
        minN = sumN[x]

print(answer)
