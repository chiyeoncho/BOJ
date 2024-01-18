import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
num = list(map(int,input().split()))
num.sort()
answer = 0

for idx in range(N):
    start = 0
    end = N - 1
    if start == idx:
        start += 1
    elif end == idx:
        end -= 1
    while start < end:
        if num[start] + num[end] > num[idx]:
            end -= 1
            if end == idx:
                end -= 1
        elif num[start] + num[end] < num[idx]:
            start += 1
            if start == idx:
                start += 1
        else:
            answer += 1
            break

print(answer)
