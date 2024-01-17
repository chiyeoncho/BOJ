import sys
input = sys.stdin.readline
n,m = map(int,input().split())
start = 1
end = 2
S = 3
count = 1

while start < end and end != n:
    if S > m:
        S-= start
        start += 1
    elif S < m:
        end += 1
        S += end
    else:
        count += 1
        end += 1
        S += end

print(count)
