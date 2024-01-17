import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int,input().split()))
stack = []
dic = dict()

for idx in range(N):
    if stack: #스택이 empty상태가 아닌 경우
        while stack and stack[-1][1] < num[idx]:
            s = stack.pop() #s는 인덱스 구하기 위해
            dic[s[0]] = num[idx]
        stack.append([idx,num[idx]])
        dic[idx] = num[idx]
    else:
        stack.append([idx,num[idx]])
        dic[idx] = num[idx]

for idx in range(N):
    if dic[idx] == num[idx]:
        print(-1,end = " ")
        continue
    print(dic[idx],end = " ")
