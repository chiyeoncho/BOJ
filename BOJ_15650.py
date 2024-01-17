import sys
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for i in range(1,N + 1):
    for j in range(i + 1,N + 1):
        graph[i].append(j)

def DFS(s,ans,m):
    if m == M:
        print(" ".join(ans))
        return
    for x in graph[s]:
        if not visited[x]:
            visited[x] = True
            ans.append(str(x))
            DFS(x,ans,m + 1)
            ans.pop()
            visited[x] = False
    if len(ans) == M:
        print(" ".join(ans))

for i in range(1,N + 1):
    ans = []
    ans.append(str(i))
    DFS(i,ans,1)
