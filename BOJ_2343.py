import sys
input = sys.stdin.readline
N,M = map(int,input().split())
lesson = list(map(int,input().split()))
end = sum(lesson)
start = max(lesson)
ans = start

while start <= end:
    mid = (start + end)//2
    s = 0
    n = 1
    for i in range(N): # 몇 개로 나뉘어질 수 있는가
        s += lesson[i]
        if s > mid:
            s = lesson[i]
            n += 1
    if n <= M:
        end = mid - 1
        ans = mid
    elif n > M:
        start = mid + 1

print(ans)
