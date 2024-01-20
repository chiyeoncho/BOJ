import sys
input = sys.stdin.readline
N = int(input())
homework = []
for _ in range(N):
    d,w = map(int,input().split())
    homework.append([w,d])
homework.sort(reverse = True)
day_off = [0 for _ in range(1001)] # 마감날이 존재하는지 확인 할 리스트
ans = 0

for w,d in homework:
    while d > 0:
        if day_off[d] == 0:
            day_off[d] = 1
            ans += w
            break
        else:
            d -= 1
print(ans)
