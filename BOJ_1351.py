import sys
from collections import defaultdict
input = sys.stdin.readline
dic = defaultdict(int)

def solution(N,P,Q):
    if N == 0:
        return 1
    elif dic[N] != 0:
        return dic[N]
    dic[N] = solution(N // P,P,Q) + solution(N // Q,P,Q)
    return dic[N]

N,P,Q = map(int,input().split())
print(solution(N,P,Q))
