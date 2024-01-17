import sys
input = sys.stdin.readline
N = int(input())
liquid = list(map(int,input().split()))
liquid.sort()

Min = 10e9
liquid1 = 0
liquid2 = 1
liquid3 = 2
for idx in range(N - 2):
    start = idx + 1
    end = N - 1
    SUM = liquid[idx]
    while start < end:
        SUM = liquid[idx] + liquid[start] + liquid[end]
        if abs(SUM) < Min:
            Min = abs(SUM)
            if SUM < 0:
                liquid1 = liquid[idx]
                liquid2 = liquid[start]
                liquid3 = liquid[end]
                start += 1
            else:
                liquid1 = liquid[idx]
                liquid2 = liquid[start]
                liquid3 = liquid[end]
                end -= 1
        else:
            if SUM < 0:
                start += 1
            else:
                end -= 1

print(liquid1,liquid2,liquid3)
