import sys
from collections import defaultdict
input = sys.stdin.readline
N,d,k,c = map(int,input().split())
sushi = []

for _ in range(N):
    n = int(input())
    sushi.append(n)

window = defaultdict(int)
cnt = 0
for i in range(k):
    window[sushi[i]] += 1
    if window[sushi[i]] == 1:
        cnt += 1

if window[c] == 0:
    cnt += 1
    ans = cnt
    cnt -= 1
else:
    ans = cnt
start = 0
end = k
for _ in range(N - 1):
    window[sushi[start]] -= 1
    window[sushi[end]] += 1
    if sushi[start] == sushi[end]:
        pass
    else:
        if window[sushi[start]] == 0:
            cnt -= 1
        if window[sushi[end]] == 1:
            cnt += 1
    start += 1
    end = (end + 1) % N
    if window[c] == 0:
        cnt += 1
        if cnt > ans:
            ans = cnt
        cnt -= 1
    elif cnt > ans:
        ans = cnt

print(ans)
