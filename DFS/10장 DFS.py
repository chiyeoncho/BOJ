# 그래프 만들기 각각 숫자에 대응되는 노드
# 1 -> A,2 -> B, 3 -> C, 4 -> D, 5 -> E, 6 -> F
# 각 행은 노드의 번호를 의미하며 행에 속해있는 데이터는 연결된 노드의 번호를 의미함.
graph = [[],
         [2, 5],
         [3],
         [4],
         [],
         [6],
         []]

visited = [False for _ in range(7)] # 방문 확인하는 리스트
def DFS(start):
    print('현재 방문 노드 {0}'.format(start))
    for x in graph[start]:
        if not visited[x]:
            visited[x] = True
            DFS(x)

DFS(1)
