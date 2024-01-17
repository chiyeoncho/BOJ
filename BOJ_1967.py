import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for _ in range(N - 1):
    u,v,w = map(int,input().split())
    tree[u].append([v,w])
    tree[v].append([u,w])

def DFS(s,now_weight):
    global MAX
    global end_node
    if now_weight > MAX:
        MAX = now_weight
        end_node = s
    for x in tree[s]:
        if not visited[x[0]]:
            visited[x[0]] = True
            DFS(x[0],now_weight + x[1])
            visited[x[0]] = False

MAX = 0
end_node = 1
visited[1] = True
DFS(1,0)
visited[1] = False
visited[end_node] = True
DFS(end_node,0)
print(MAX)
