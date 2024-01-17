import sys
from _collections import deque
input = sys.stdin.readline
N,L = map(int,input().split())
window = deque()
answer = []

num = list(map(int,input().split()))

for idx in range(N):
    if window: #윈도우가 존재하는 경우
        finish = False
        while window and finish == False:
            if window[-1][1] > num[idx]:
                window.pop()
            else:
                finish = True
        window.append([idx,num[idx]])
        if idx - window[0][0] >= L: #맨 앞을 제거해야하는 경우(인덱스 벗어남)
            window.popleft()
    else: #윈도우가 존재하지 않는 경우
        window.append([idx,num[idx]])
    answer.append(window[0][1])

for x in answer:
    print(x,end = " ")
