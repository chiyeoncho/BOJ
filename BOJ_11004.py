import sys
input = sys.stdin.readline

N,K = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
print(num[K - 1])

#퀵 정렬 이용하여 다시 풀기
