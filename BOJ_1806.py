import sys
input = sys.stdin.readline
N,S = map(int,input().split())
num = list(map(int,input().split()))

start = 0
end = 0
add = num[0]
ans = 10e9
n = 1
while start <= end and end < N:
    if add >= S:
        add -= num[start]
        start += 1
        if n < ans:
            ans = n
        n -= 1
    else:
        end += 1
        if end < N:
            add += num[end]
        n += 1
if ans == 10e9:
    print(0)
else:
    print(ans)
