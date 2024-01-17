import sys
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

print(D[n2][n1])
