import sys
input = sys.stdin.readline
N,K = map(int,input().split())
D = [[1 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(2,N + 1):
    for j in range(K + 1):
        if j == 0 or i == j:
            D[i][j] = 1
            continue
        D[i][j] = (D[i - 1][j] + D[i - 1][j - 1]) % 10007

print(D[N][K])
