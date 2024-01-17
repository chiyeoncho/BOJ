import sys
input = sys.stdin.readline
N = int(input())
day = []
for i in range(N):
    T,P = map(int,input().split())
    day.append([T,P])
D = [-1 for _ in range(N + 1)]

def DFS(start,price):
    global MAX
    if price > MAX:
        MAX = price
    for i in range(start + day[start][0],N):
        if i + day[i][0] <= N:
            DFS(i,price + day[i][1])

MAX = 0
for i in range(N):
    if i + day[i][0] <= N:
            DFS(i,day[i][1])

print(MAX)
