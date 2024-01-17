import sys
import heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
hq = []
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
D = [1000000000 for _ in range(N + 1)] # 최단 경로 리스트

for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append([v,w]) # 가중치 방향 그래프 표현

start,end = map(int,input().split()) # 최단 거리 원하는 노드 입력
D[start] = 0
heapq.heappush(hq,(0,start)) # 힙 이용

while hq:
    now = heapq.heappop(hq) # 현재의 노드 위치
    now_distance = now[0] # 현재까지의 경로
    if visited[now[1]]:
        continue
    visited[now[1]] = True
    for i in graph[now[1]]: # 현재의 노드 위치와 연결되어있는 노드 확인하기
        if D[i[0]] > i[1] + now_distance:
            D[i[0]] = i[1] + now_distance
            heapq.heappush(hq,(D[i[0]],i[0]))

print(D[end])
