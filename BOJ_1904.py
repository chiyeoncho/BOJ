import sys
input = sys.stdin.readline
N = int(input())
D = [-1 for _ in range(N + 1)]
if N >= 2:
    D[1] = 1
    D[2] = 2
else:
    D[1] = 1

for i in range(3,N + 1):
    D[i] = (D[i - 1] + D[i - 2]) % 15746

print(D[N])
