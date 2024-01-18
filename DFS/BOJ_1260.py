import sys
from collections import deque
input = sys.stdin.readline
def DFS(graph,V):
    visited1[V] = True
    print(V,end = " ")
    for x in graph[V]:
        if not visited1[x]:
            DFS(graph,x)

def BFS(graph,V):
    queue = deque(graph[V])
    print(V,end = " ")
    visited2[V] = True
    while len(queue) > 0:
        n = len(queue)
        for i in range(n):
            if not visited2[queue[0]]:
                for k in graph[queue[0]]:
                    queue.append(k)
                print(queue[0],end = " ")
                visited2[queue[0]] = True
            queue.popleft()

N,M,V = map(int,input().split())
graph = [[] for _ in range(N + 1)]
visited1 = [False for _ in range(N + 1)]
visited2 = [False for _ in range(N + 1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N + 1):
    graph[i].sort()

DFS(graph,V)
print()
BFS(graph,V)
