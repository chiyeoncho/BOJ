import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[] for _ in range(N + 1)]
D = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    D[v] += 1

queue = deque()
for i in range(1,N + 1):
    if D[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    visited[now] = True
    for i in graph[now]:
        D[i] -= 1
        if not visited[i] and D[i] == 0:
            queue.append(i)
    print(now,end = ' ')
