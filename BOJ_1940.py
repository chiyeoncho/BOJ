import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
num = list(map(int,input().split()))
num.sort()

start = 0
end = N - 1
answer = 0
SUM = num[start] + num[end]

while start < end:
    if SUM > M:
        end -= 1
        SUM = num[start] + num[end]
    elif SUM < M:
        start += 1
        SUM = num[start] + num[end]
    else:
        answer += 1
        start += 1
        SUM = num[start] + num[end]

print(answer)
