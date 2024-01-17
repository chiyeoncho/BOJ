import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
N = int(input())
tree = dict()
tree[1] = 1
parents = [1 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

def DFS(n):
    for x in graph[n]:
        if n in tree and x in tree:
            continue
        elif n in tree:
            parents[x] = n
            tree[x] = 1
        elif x in tree:
            parents[n] = x
            tree[n] = 1
        else:
            parents[n] = x
            parents[x] = n
        if not visited[x]:
            visited[x] = True
            DFS(x)
for _ in range(N - 1):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(1,N + 1):
    DFS(i)

for i in range(2,N + 1):
    print(parents[i])
