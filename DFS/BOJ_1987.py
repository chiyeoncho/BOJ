import sys
input = sys.stdin.readline
R, C = map(int,input().split())
board = []

for _ in range(R):
    word = input().rstrip()
    board.append(word)

MAX = 0
dic = {}
dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y, n):
    global MAX
    global dic
    if n > MAX:
        MAX = n
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in dic:
            dic[board[nx][ny]] = 1
            DFS(nx, ny, n + 1)
            del dic[board[nx][ny]]

dic[board[0][0]] = 1
DFS(0, 0, 1)
print(MAX)
