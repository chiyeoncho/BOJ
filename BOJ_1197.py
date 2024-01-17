import sys
input = sys.stdin.readline
V,E = map(int,input().split())
EdgeGraph = []
parents = [i for i in range(V + 1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    EdgeGraph.append([w,u,v])
EdgeGraph.sort()

def find(n):
    if parents[n] == n:
        return n
    else:
        parents[n] = find(parents[n])
        return parents[n]

def union(n,m):
    n = find(n)
    m = find(m)
    if n != m:
        parents[m] = n

def IsSame(n,m):
    n = find(n)
    m = find(m)
    if n == m:
        return True
    return False

ans = 0
for data in EdgeGraph:
    u,v,w = data[1],data[2],data[0]
    if not IsSame(u,v):
        union(u,v)
        ans += w

print(ans)
