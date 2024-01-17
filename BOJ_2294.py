import sys
input = sys.stdin.readline
n,k = map(int,input().split())
coin = []

for _ in range(n):
    c = int(input())
    if c in coin:
        continue
    coin.append(c)
coin.sort()
dp = [10000000000 for _ in range(k + 1)]
dp[0] = 0

for c in coin:
    for i in range(c,k + 1):
        dp[i] = min(dp[i],dp[i - c] + 1)

if dp[k] == 10000000000:
    print(-1)
else:
    print(dp[k])
