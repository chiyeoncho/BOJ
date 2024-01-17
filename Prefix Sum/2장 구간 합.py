num = [7, 4, 5, 6, 9, 10, 1]
SUM = []
SUM.append(num[0])

for i in range(1,len(num)):
    SUM.append(SUM[i - 1] + num[i])

print(SUM)
