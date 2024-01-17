import sys
input = sys.stdin.readline
N,M = map(int,input().split())
num1 = list(map(int,input().split()))
num1.sort()
graph = [[] for _ in range(10001)]
num = []
for x in num1:
    if x not in num:
        num.append(x)

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
