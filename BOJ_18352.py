import sys
input = sys.stdin.readline
def find(start,distance,p):
    if p >= K:
        return
    for i in graph[start]:
        if distance[i] > p + 1:
            distance[i] = p + 1
            find(i,distance,p + 1)

N,M,K,X = map(int,input().split())
graph = [[] for _ in range(N + 1)]
distance = [10000000000 for _ in range(N + 1)]
distance[X] = 0
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
find(X,distance,0)
ans = 0
for i in range(1,N + 1):
    if distance[i] == K:
        ans += 1
        print(i)
if ans == 0:
    print(-1)
