import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
D = [1 for _ in range(N)]

MAX = 1
for i in range(N - 2,-1,-1):
    for j in range(i + 1,N):
        if A[j] > A[i]:
            D[i] = max(D[i],1 + D[j])
            if D[i] > MAX:
                MAX = D[i]

print(MAX)
