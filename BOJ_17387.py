import sys
input = sys.stdin.readline
x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

ccw1 = (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)
ccw2 = (x1 * y2 + x2 * y4 + x4 * y1) - (y1 * x2 + y2 * x4 + y4 * x1)
ccw3 = (x3 * y4 + x4 * y1 + x1 * y3) - (y3 * x4 + y4 * x1 + y1 * x3)
ccw4 = (x3 * y4 + x4 * y2 + x2 * y3) - (y3 * x4 + y4 * x2 + y2 * x3)
X1Min = min(x1,x2)
X1Max = max(x1,x2)
X2Min = min(x3,x4)
X2Max = max(x3,x4)
Y1Min = min(y1,y2)
Y1Max = max(y1,y2)
Y2Min = min(y3,y4)
Y2Max = max(y3,y4)

if (ccw1 > 0 and ccw2 > 0) or (ccw1 < 0 and ccw2 < 0) or (ccw3 > 0 and ccw4 > 0) or (ccw3 < 0 and ccw4 < 0):
    print(0)
elif ccw1 == ccw2: # 기울기가 같은 경우
    if x1 - x2 == 0: # y를 사용해야하는 경우(기울기가 정의되지 않는 경우)
        if Y1Min < Y2Min:
            if Y1Max >= Y2Min:
                print(1)
            else:
                print(0)
        elif Y1Min > Y2Min:
            if Y2Max >= Y1Min:
                print(1)
            else:
                print(0)
        else:
            print(1)
    else: # x를 사용하는 경우
        if X1Min < X2Min:
            if X1Max >= X2Min:
                print(1)
            else:
                print(0)
        elif X1Min > X2Min:
            if X2Max >= X1Min:
                print(1)
            else:
                print(0)
        else:
            print(1)
else:
    print(1)
