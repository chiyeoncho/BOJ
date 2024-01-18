import sys
input = sys.stdin.readline
N = int(input())
house = []
for _ in range(N):
    data = list(map(int,input().split()))
    house.append(data)
D = [[0 for _ in range(3)] for _ in range(N)]
D[N - 1][0] = house[N - 1][0]
D[N - 1][1] = house[N - 1][1]
D[N - 1][2] = house[N - 1][2]
for i in range(N - 2,-1,-1):
    D[i][0] = min(house[i][0] + D[i + 1][1],house[i][0] + D[i + 1][2])
    D[i][1] = min(house[i][1] + D[i + 1][0],house[i][1] + D[i + 1][2])
    D[i][2] = min(house[i][2] + D[i + 1][0],house[i][2] + D[i + 1][1])
print(min(D[0][0],D[0][1],D[0][2]))
