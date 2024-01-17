import sys
input = sys.stdin.readline
n,m = map(int,input().split())
parents = [i for i in range(n + 1)]

def find(n):
    if parents[n] == n:
        return n
    parents[n] = find(parents[n])
    return parents[n]

def merge(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    parents[y] = x

def IsUnion(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return True
    return False

for _ in range(m):
    d1, d2, d3 = map(int,input().split())
    if d1 == 0:
        merge(d2,d3)
    elif d1 == 1:
        if IsUnion(d2,d3):
            print("YES")
        else:
            print("NO")
