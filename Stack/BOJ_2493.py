import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
top = list(map(int,input().split()))
stack = []
dic = defaultdict(int)

for idx in range(N - 1,-1,-1):
    if len(stack) == 0:
        stack.append(top[idx])
    else:
        while True:
            if len(stack) == 0 or stack[-1] > top[idx]:
                stack.append(top[idx])
                break
            else:
                dic[stack.pop()] = idx + 1

for i in range(N):
    print(dic[top[i]],end = ' ')
