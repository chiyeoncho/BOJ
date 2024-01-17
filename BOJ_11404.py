# 플로이드
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
D = [[100000000000 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1,n + 1):
    D[i][i] = 0

for _ in range(m):
    u,v,e = map(int,input().split())
    graph[u].append([v,e])
    D[u][v] = min(D[u][v],e)

for k in range(1,n + 1):
    for j in range(1,n + 1):
        for i in range(1,n + 1):
            D[j][i] = min(D[j][i],D[j][k] + D[k][i])

for i in range(1,n + 1):
    for j in range(1,n + 1):
        if D[i][j] == 100000000000:
            print(0,end = " ")
        else:
            print(D[i][j],end = " ")
    print()
