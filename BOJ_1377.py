import sys
input = sys.stdin.readline

N = int(input())
num = []
ch = []

for idx in range(N):
    n = int(input())
    num.append([n,idx])

num.sort()
answer = 0
for idx in range(N):
    answer = max(answer,num[idx][1] - idx)

print(answer + 1)
