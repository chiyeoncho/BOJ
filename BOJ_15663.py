import sys
input = sys.stdin.readline
N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
graph = [[] for _ in range(10001)]
visited = [False for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            graph[i].append([num[j],j])

dic = {}
def DFS(s,m,ans):
    if m == M and " ".join(ans) not in dic:
        print(" ".join(ans))
        dic[" ".join(ans)] = 1
        return
    elif m == M:
        return
    for x in graph[s]:
        if not visited[x[1]]:
            visited[x[1]] = True
            ans.append(str(x[0]))
            DFS(x[1],m + 1,ans)
            ans.pop()
            visited[x[1]] = False

for i in range(N):
    ans = []
    visited[i] = True
    ans.append(str(num[i]))
    DFS(i,1,ans)
    visited[i] = False
