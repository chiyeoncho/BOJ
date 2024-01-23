import sys
input = sys.stdin.readline
L,C = map(int,input().split())
alphabet = list(input().rstrip().split())
alphabet.sort()
dic = {}
dic[0] = 0 # 자음 수
dic[1] = 0 # 모음 수
visited = [False for _ in range(26)]

def DFS(ans, n, y):
    global dic
    if n == L and dic[0] >= 2 and dic[1] >= 1:
        print(''.join(ans))
        return
    elif n == L:
        return
    for x in range(C):
        if not visited[x] and x > y:
            visited[x] = True
            ans.append(alphabet[x])
            if alphabet[x] == 'a' or alphabet[x] == 'e' or alphabet[x] == 'i' or alphabet[x] == 'o' or alphabet[x] == 'u':
                dic[1] += 1
                DFS(ans, n + 1, x)
                dic[1] -= 1
            else:
                dic[0] += 1
                DFS(ans,n + 1, x)
                dic[0] -= 1
            visited[x] = False
            ans.pop()

ans = []
DFS(ans, 0, -1)
