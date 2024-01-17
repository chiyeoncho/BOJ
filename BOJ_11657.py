# 벨만 포드 알고리즘 연습
import sys
input = sys.stdin.readline
N,M = map(int,input().split())

EdgeGraph = []
D = [1000000000 for _ in range(N + 1)]
D[1] = 0
for _ in range(M):
    u,v,w = map(int,input().split())
    EdgeGraph.append([u,v,w])

for _ in range(N - 1):
    for data in EdgeGraph:
        s = data[0] # 시작점
        v = data[1] # 끝
        w = data[2] # 가중치
        if D[v] > D[s] + w and D[s] != 1000000000:
            D[v] = D[s] + w

no = False
for data in EdgeGraph:
    s = data[0] # 시작점
    v = data[1] # 끝
    w = data[2] # 가중치
    if D[v] > D[s] + w and D[s] != 1000000000:
        no = True
        break

if no :
    print(-1)
else:
    for i in range(2,N + 1):
        if D[i] == 1000000000:
            print(-1)
        else:
            print(D[i])
