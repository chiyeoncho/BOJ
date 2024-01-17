import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
dic = {}

def fibonacci(fn):
    global cnt0
    global cnt1
    if fn == 0:
        cnt0 += 1
        return 0
    elif fn == 1:
        cnt1 += 1
        return 1
    elif fn in dic:
        cnt1 += dic[fn][0]
        cnt0 += dic[fn][1]
        return 0

    fibonacci(fn - 1), fibonacci(fn - 2)
    dic[fn] = [cnt1,cnt0]

for _ in range(N):
    cnt0 = 0
    cnt1 = 0
    fn = int(input())
    fibonacci(fn)
    print(cnt0,cnt1)
