import sys
input = sys.stdin.readline
N = int(input())
findXY = []

for _ in range(N):
    x, y = map(int,input().split())
    findXY.append([x, y])
findXY.append(findXY[0])

ans = 0
for i in range(N):
    ans += (findXY[i][0] * findXY[i + 1][1]) - (findXY[i + 1][0] * findXY[i][1])

print("{:.1f}".format(abs(ans) / 2))
