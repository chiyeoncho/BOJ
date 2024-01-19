num = [7, 6, 1, 3, 4, 2]
N = len(num)

for i in range(N):
    MinIdx = i # 최솟값 인덱스 초기화
    for j in range(i + 1,N):
        if num[MinIdx] > num[j]: # 인덱스 초기화 조건
            MinIdx = j
    temp = num[MinIdx] # Swap
    num[MinIdx] = num[i]
    num[i] = temp

print(num)
