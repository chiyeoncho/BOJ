import sys
input = sys.stdin.readline
N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
graph = [[] for _ in range(10001)]

for x in num:
    for y in num:
        if y >= x:
            graph[x].append(y)

def DFS(s,m,ans):
    if m == M:
        print(" ".join(ans))
        return
    for x in graph[s]:
        ans.append(str(x))
        DFS(x,m + 1,ans)
        ans.pop()

for x in num:
    ans = []
    ans.append(str(x))
    DFS(x,1,ans)
