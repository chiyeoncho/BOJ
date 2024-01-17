import sys
input = sys.stdin.readline
N,K = map(int,input().split())
num = list(input().rstrip())
cnt = 0
stack = []
for x in num:
    if not stack:
        stack.append(x)
    else:
        if cnt == K:
                stack.append(x)
                continue
        while len(stack) != 0 and int(stack[-1]) < int(x) and cnt != K:
            stack.pop()
            cnt += 1
        stack.append(x)
while cnt < K:
    stack.pop()
    cnt += 1
print("".join(stack))
