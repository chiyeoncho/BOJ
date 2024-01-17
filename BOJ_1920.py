import sys
input = sys.stdin.readline
N = int(input())
data = list(map(int,input().split()))
M = int(input())
find = list(map(int,input().split()))
data.sort()

for f in find:
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right)//2
        if data[mid] > f:
            right = mid - 1
        elif data[mid] < f:
            left = mid + 1
        else:
            print(1)
            break
    if left > right:
        print(0)
