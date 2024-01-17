import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
n = int(input())
D = [0 for _ in range(n + 1)]
if n >= 2:
    D[1] = 1
    D[2] = 2
else:
    D[1] = 1

def tile(n):
    if D[n] != 0:
        return D[n]
    D[n] = (tile(n - 1) + tile(n - 2)) % 10007
    return D[n]

print(tile(n))
