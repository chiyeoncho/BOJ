import sys
input = sys.stdin.readline

N = int(input())

start,end = 1,1
SUM = 1
cnt1,cnt2=1,1
answer = 0

while start <= end:
    if SUM > N:
        start += 1
        SUM -= cnt1
        cnt1 += 1
    elif SUM < N:
        end += 1
        cnt2 += 1
        SUM += cnt2
    else:
        answer += 1
        cnt2 += 1
        SUM += cnt2
        end += 1

print(answer)
