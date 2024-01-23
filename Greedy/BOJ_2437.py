import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int,input().split()))
num.sort()
SUM = []
SUM.append(num[0])
for i in range(1, N):
    SUM.append(num[i] + SUM[i - 1])

finish = False
if SUM[0] == 1:
    for i in range(1, N):
        if num[i] > SUM[i - 1] + 1:
            print(SUM[i - 1] + 1)
            finish = True
            break
else:
    print(1)
    finish = True

if not finish:
    print(sum(num) + 1)
