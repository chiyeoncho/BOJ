import sys
input = sys.stdin.readline
N = int(input())
square = []
D = [[0 for _ in range(500)] for _ in range(500)]

for i in range(N):
    data = list(map(int,input().split()))
    for j in range(i + 1):
        D[i][j] = data[j]

for i in range(N - 2,-1,-1):
    for j in range(i,-1,-1):
        D[i][j] = max(D[i][j] + D[i + 1][j],D[i][j] + D[i + 1][j + 1])

print(D[0][0])
