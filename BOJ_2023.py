import sys
input = sys.stdin.readline
def find_decimal(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True

def DFS(N,digit,num):
    if digit > N:
        return
    for i in range(1,10):
        if find_decimal(num * 10 + i) == True: #소수라면
            if digit == N:
                print(num * 10 + i)
            DFS(N,digit + 1,num * 10 + i)
    return

N = int(input())
digit = 1
answer = []

DFS(N,digit,0)
