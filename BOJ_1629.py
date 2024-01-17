import sys
input = sys.stdin.readline
A,B,C = map(int,input().split())

def dp(n):
    if n == 1:
        return A % C
    elif n == 2:
        return (A * A) % C
    if n % 2 != 0:
        return ((dp(n // 2) ** 2) * A) % C
    else:
        return (dp(n // 2) ** 2) % C

print(dp(B))
