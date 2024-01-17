import sys
from collections import deque
input = sys.stdin.readline

def BFS(graph,start):
    global cnt
    visited = [False for _ in range(10001)]
    visited[start] = True
    queue = deque()
    queue.append(start)
    while queue:
        now_node = queue.popleft()
        for n in graph[now_node]:
            if not visited[n]:
                visited[n] = True
                cnt += 1
                queue.append(n)

N,M = map(int,input().split())
graph = [[] for _ in range(N + 1)]
count = [0 for _ in range(N + 1)]

for _ in range(M):
    u,v = map(int,input().split())
    graph[v].append(u)

MAX = 0
for i in range(1,N + 1):
    cnt = 0
    BFS(graph,i)
    count[i] = cnt
    if cnt > MAX:
        MAX = cnt

for i in range(1,N + 1):
    if count[i] == MAX:
        print(i,end = ' ')
