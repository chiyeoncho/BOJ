import sys
input = sys.stdin.readline
XY = []
for _ in range(3):
    x,y = map(int,input().split())
    XY.append([x,y])
ccw = (XY[0][0] * XY[1][1] + XY[1][0] * XY[2][1] + XY[2][0] * XY[0][1]) - (XY[0][1] * XY[1][0] + XY[1][1] * XY[2][0] + XY[2][1] * XY[0][0])

if ccw < 0:
    print(-1)
elif ccw == 0:
    print(0)
else:
    print(1)
