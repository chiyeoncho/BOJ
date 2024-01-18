import sys
input = sys.stdin.readline
N = int(input())
data = list(map(int,input().split()))
tree = [[] for _ in range(N)]
delete = int(input())
start = int()
visited = [False for _ in range(N)]
visited[delete] = True

def DFS(n):
    global ans
    cnt = 0
    if visited[n]:
        return
    visited[n] = True
    for x in tree[n]:
        if not visited[x]:
            cnt += 1
            DFS(x)
    if cnt == 0:
        ans += 1

for x in range(N):
    if data[x] == -1:
        start = x
    else:
        tree[data[x]].append(x) # 방향 그래프 작성

ans = 0
DFS(start)
print(ans)
