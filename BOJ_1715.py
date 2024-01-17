import sys
import heapq
input = sys.stdin.readline
N = int(input())
card = []
ans = 0

for _ in range(N):
    n = int(input())
    heapq.heappush(card,n)

while len(card) > 1:
    shuffle1 = heapq.heappop(card)
    shuffle2 = heapq.heappop(card)
    s = shuffle1 + shuffle2
    ans += s
    heapq.heappush(card,s)

print(ans)
