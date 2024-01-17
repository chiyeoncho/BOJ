import sys
from _collections import defaultdict
input = sys.stdin.readline

N,M = map(int,input().split())
num = list(map(int,input().split()))
SUM = 0
part_rest = []
answer = 0
dic = defaultdict(int)
dic[0] = 1

for x in num:
    SUM += x
    answer += dic[SUM % M]
    dic[SUM % M] += 1

print(answer)
