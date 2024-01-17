import sys
input = sys.stdin.readline

A,B = map(int,input().split())
num = [0 for _ in range(int(B**0.5 + 1))]
ans = 0

for i in range(2,int(B**0.5 + 1)):
    if num[i] == 1:
        continue
    else:
        for j in range(i * 2,int(B**0.5 + 1),i):
            num[j] = 1
        d = i
        while i <= B / d:
            if i * d >= A:
                ans += 1
            d *= i
print(ans)
