import sys
input = sys.stdin.readline
S = list(input().rstrip())
T = list(input().rstrip())
IsSame = False

while len(S) <= len(T):
    if ''.join(S) == ''.join(T):
        IsSame = True
        break
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T = T[::-1]

if IsSame:
    print(1)
else:
    print(0)
