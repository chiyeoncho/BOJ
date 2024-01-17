import sys
from collections import deque
input = sys.stdin.readline
str1 = list(input().rstrip())
str2 = list(input().rstrip())
n1 = len(str1)
n2 = len(str2)
D = [[0 for _ in range(n1 + 1)] for _ in range(n2 + 1)]
for i in range(1,n2 + 1):
    for j in range(1,n1 + 1):
        if str1[j - 1] == str2[i - 1]:
            D[i][j] = D[i - 1][j - 1] + 1
        else:
            D[i][j] = max(D[i][j - 1],D[i - 1][j])
ans = deque()
start1 = n1
start2 = n2
for i in range(n2,0,-1):
    if start1 == 0 or start2 == 0:
            break
    for j in range(n1,0,-1):
        if start1 == 0 or start2 == 0:
            break
        if str1[start1 - 1] == str2[start2 - 1]:
            ans.appendleft(str2[start2 - 1])
            start1 -= 1
            start2 -= 1
        else:
            if D[start2 - 1][start1] > D[start2][start1 - 1]: # 위쪽이 더 큰 경우
                start2 -= 1
            else:
                start1 -= 1

if D[n2][n1] == 0:
    print(D[n2][n1])
else:
    print(D[n2][n1])
    print("".join(ans))
