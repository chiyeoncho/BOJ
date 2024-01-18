import sys
from collections import deque
input = sys.stdin.readline
def BFS(graph):
    global ans
    global start
    visited[start] = True
    queue = deque()
    queue.append(start)
    nd = deque()
    nd.append(0)
    while queue:
        for i in range(len(queue)):
            n = queue.popleft()
            now_distance = nd.popleft()
            for x,weight in graph[n]:
                if not visited[x]:
                    visited[x] = True
                    queue.append(x)
                    nd.append(now_distance + weight)
                    if now_distance + weight > ans:
                        ans = now_distance + weight
                        start = x

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    data = list(map(int,input().split()))
    start = data[0]
    for i in range(1,len(data) - 1,2):
        graph[start].append([data[i],data[i + 1]])

ans = 0
start = 1
for i in range(2):
    visited = [False for _ in range(V + 1)]
    BFS(graph)

print(ans)
