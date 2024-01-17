import sys
input = sys.stdin.readline

N = int(input())
num = input().rstrip()
SUM = 0

for x in num:
    SUM += int(x)
print(SUM)
