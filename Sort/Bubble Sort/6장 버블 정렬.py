num = [7, 6, 1, 3, 4, 2]
N = len(num)
for i in range(N):
    for j in range(i + 1,N):
        if num[i] > num[j]: # Swap
            temp = num[i]
            num[i] = num[j]
            num[j] = temp

print(num)
