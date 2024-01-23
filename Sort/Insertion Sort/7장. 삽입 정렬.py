num = [7, 3, 9, 5, 4, 1, 2]
N = len(num)

for i in range(1, N):
    for j in range(i, 0, -1):
        if num[j - 1] > num[j]:
            temp = num[j]
            num[j] = num[j - 1]
            num[j - 1] = temp
        else:
            break

print(num)
