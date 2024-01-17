import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
finish = False

for answer in range(10000):
    up_num = 0
    down_num = 0
    same_num = 0
    for x in a:
        if x > answer:
            up_num += 1
        elif x < answer:
            down_num += 1
        else:
            same_num += 1
    if up_num + same_num >= answer:
        for i in range(same_num + 1):
            if down_num + i == n - answer:
                print(answer)
                finish = True
                break
    if finish == True:
        break
