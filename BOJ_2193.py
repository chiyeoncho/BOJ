import sys
input = sys.stdin.readline
dic = {}
dic[1] = 1
dic[2] = 1
def pinary_number(N):
    if N in dic:
        return dic[N]
    dic[N] = pinary_number(N - 2) + pinary_number(N - 1)
    return dic[N]

N = int(input())
print(pinary_number(N))
