#삽입정렬 이용하기
import sys
input = sys.stdin.readline

N = int(input())
person = list(map(int,input().split()))

for i in range(1,N):
    insert_point = i
    temp = person[i]
    for j in range(i - 1,-1,-1):
        if person[j] < person[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i,insert_point,-1):
        person[j] = person[j - 1]
    person[insert_point] = temp

SUM = [0]*N
SUM[0] = person[0]

for i in range(1,N):
    SUM[i] = SUM[i - 1] + person[i]
answer = 0

for i in range(N):
    answer += SUM[i]

print(answer)
