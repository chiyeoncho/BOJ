import sys
input = sys.stdin.readline
n,k = map(int,input().split())
coin = []

for _ in range(n):
    c = int(input())
    coin.append(c)
coin.sort()

dp = [0 for _ in range(k + 1)]
dp[0] = 1

for C in coin:
    for i in range(C,k + 1):
        dp[i] = dp[i] + dp[i - C]

print(dp[k])
