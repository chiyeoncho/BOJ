import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    TeList = []
    for i in range(n):
        tel = input().rstrip()
        TeList.append(tel)
    TeList.sort()
    dic = dict()
    IsCons = True
    for i in range(n):
        if not IsCons:
            break
        LEN = len(TeList[i])
        for j in range(LEN - 1, 0, -1):
            if ''.join(TeList[i][:j]) in dic:
                IsCons = False
                break
        dic[''.join(TeList[i])] = 1
    if IsCons:
        print("YES")
    else:
        print("NO")
