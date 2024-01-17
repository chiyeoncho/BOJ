import sys
input = sys.stdin.readline
N = int(input())

def find_prime(n):
    for i in range(2,int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True

prime_num = []
for i in range(2,N + 1):
    if find_prime(i):
        prime_num.append(i)

n = len(prime_num)
if N == 1:
    print(0)
else:
    start = end = 0
    S = prime_num[0]
    count = 0
    while end != n:
        if S > N:
            S -= prime_num[start]
            start += 1
        elif S < N:
            end += 1
            if end != n:
                S += prime_num[end]
        else:
            count += 1
            end += 1
            if end != n:
                S += prime_num[end]
    print(count)
