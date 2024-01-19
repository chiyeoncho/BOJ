import sys
input = sys.stdin.readline
N,M = map(int,input().split())
num = []

for _ in range(N):
    num.append(int(input()))

num.sort()
start = 0
end = 0
MIN = 10e9

while start <= end and end < N:
    difference = num[end] - num[start]
    if difference < M:
        end += 1
    else:
        if difference < MIN:
            MIN = difference
        start += 1
print(MIN)
