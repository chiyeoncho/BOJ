import sys
input = sys.stdin.readline
N, M = map(int,input().split())
board = []
OriginSafety = 0
check = [[0 for _ in range(M)] for _ in range(N)]
MAX = 0
NoSafe = int()

for _ in range(N):
    data = list(map(int,input().split()))
    OriginSafety += data.count(0)
    board.append(data)

dx = [-1, 0, 1 ,0]
dy = [0, 1, 0, -1]
def VirusCheck(x, y): # 바이러스가 얼마나 퍼지는지 카운트하는 함수
    global NoSafe
    global check
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and check[nx][ny] == 0:
            check[nx][ny] = 1
            NoSafe += 1
            VirusCheck(nx, ny)

def Construction(n): # 기둥을 건설하는 함수
    if n == 3:
        Check()
        return
    else:
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    board[i][j] = 1
                    Construction(n + 1)
                    board[i][j] = 0

def Check(): # 기둥이 3개 건설되었을 때 확인하는 함수
    global MAX
    global NoSafe
    global check
    NoSafe = 0
    check = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                VirusCheck(i, j)
    if OriginSafety - NoSafe - 3 > MAX:
        MAX = OriginSafety - NoSafe - 3

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            board[i][j] = 1
            Construction(1)
            board[i][j] = 0

print(MAX)
