import sys
input = sys.stdin.readline
cnt = 0

def DFS(graph,start):
    if ch[start] != 0:
        return
    else:
        ch[start] = 1
        for x in graph[start]:
            if ch[x] == 0:
                DFS(graph,x)

N,M = map(int,input().split())
graph = [[] for _ in range(N + 1)]
ch = [0 for _ in range(N + 1)]

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N + 1):
    if ch[i] == 0:
        cnt += 1
        DFS(graph,i)

print(cnt)
