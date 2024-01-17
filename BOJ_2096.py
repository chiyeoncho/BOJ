import sys
input = sys.stdin.readline
N = int(input())
D = [[0 for _ in range(3)] for _ in range(N)]
d = [[0 for _ in range(3)] for _ in range(N)]

for i in range(N):
    data = list(map(int,input().split()))
    for j in range(3):
        D[i][j] = data[j]
        d[i][j] = data[j]

for i in range(N - 2,-1,-1):
    for j in range(2,-1,-1):
        if j == 0:
            D[i][j] = max(D[i][j] + D[i + 1][j],D[i][j] + D[i + 1][j + 1])
            d[i][j] = min(d[i][j] + d[i + 1][j],d[i][j] + d[i + 1][j + 1])
        elif j == 1:
            D[i][j] = max(D[i][j] + D[i + 1][j],D[i][j] + D[i + 1][j + 1],D[i][j] + D[i + 1][j - 1])
            d[i][j] = min(d[i][j] + d[i + 1][j],d[i][j] + d[i + 1][j + 1],d[i][j] + d[i + 1][j - 1])
        else:
            D[i][j] = max(D[i][j] + D[i + 1][j - 1],D[i][j] + D[i + 1][j])
            d[i][j] = min(d[i][j] + d[i + 1][j - 1],d[i][j] + d[i + 1][j])

print(max(D[0][0],D[0][1],D[0][2]),min(d[0][0],d[0][1],d[0][2]))
