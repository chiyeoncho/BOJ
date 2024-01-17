import sys
input = sys.stdin.readline
A,B = map(int,input().split())
square = []

for i in range(2,int(B**0.5 + 1)):
    square.append(i * i)

cnt = B - A + 1
dic = {}

for x in square:
    start = x
    if x not in dic:
        if start < A:
            if A % start == 0:
                start = A
            else:
                start = start * (A // start + 1)
        for i in range(start,B + 1,x):
            if i not in dic:
                cnt -= 1
                dic[i] = 1

print(cnt)
