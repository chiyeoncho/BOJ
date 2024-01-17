import sys
input = sys.stdin.readline
N = int(input())
L = [0 for _ in range(N)]
R = [0 for _ in range(N)]
num = list(map(int,input().split()))
L[0] = num[0]
R[N - 1] = num[N - 1]
ans = num[0]
for i in range(1,N):
    L[i] = max(num[i],L[i - 1] + num[i])
    if ans < L[i]:
        ans = L[i]
for i in range(N - 2,-1,-1):
    R[i] = max(num[i],R[i + 1] + num[i])

for i in range(1,N - 1):
    if L[i - 1] + R[i + 1] > ans:
        ans = L[i - 1] + R[i + 1]

print(ans)
