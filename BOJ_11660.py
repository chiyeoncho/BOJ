import sys
input = sys.stdin.readline

N,M = map(int,input().split())
board_sum = [[] for _ in range(N + 1)]
answer = []

for idx in range(N + 1): #board 만들기
    if idx == 0:
        for _ in range(N + 1):
            board_sum[idx].append(0)
        continue
    board_sum[idx].append(0)
    line = list(map(int,input().split()))
    SUM = 0
    if idx == 1:
        for x in line:
            SUM += x
            board_sum[idx].append(SUM)
    else:
        for idy in range(1,N + 1):
            board_sum[idx].append(board_sum[idx - 1][idy] + board_sum[idx][idy - 1] + line[idy - 1] - board_sum[idx - 1][idy - 1])

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    answer.append(board_sum[x2][y2] - board_sum[x1 - 1][y2] - board_sum[x2][y1 - 1] + board_sum[x1 - 1][y1 - 1])

for a in answer:
    print(a)
