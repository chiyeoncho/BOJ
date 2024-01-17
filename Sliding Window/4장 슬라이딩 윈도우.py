num = [1, 2, 1, 5, 7, 4, 3]
list_len = len(num) # 리스트의 길이
n = 3 # 윈도우의 길이
window = 0

for i in range(n):
    window += num[i]

MAX = window # 처음 최댓값
start = 0 # 처음 윈도우에서 뺄 인덱스
end = n # 처음 윈도우에서 더할 인덱스

while end < list_len:
    window -= num[start]
    window += num[end]
    start += 1
    end += 1
    if window > MAX:
        MAX = window

print(MAX)
