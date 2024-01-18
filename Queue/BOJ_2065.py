import sys
from collections import deque
input = sys.stdin.readline
M,t,N = map(int,input().split())
customer_R = []
customer_L = []
ferry = [0,"left"]
ans = []

for idx in range(N):
    time,position = input().split()
    time = int(time)
    if position == "right":
        customer_R.append([time,position,idx])
    else:
        customer_L.append([time,position,idx])
customer_R.sort()
customer_L.sort()
customer_R = deque(customer_R)
customer_L = deque(customer_L)

while customer_R or customer_L:
    if customer_R and customer_L and customer_R[0][0] > customer_L[0][0]:
        if ferry[1] == "left":
            n = 1
            data = list(customer_L.popleft())
            time = max(data[0],ferry[0])
            data[0] = time + t
            ans.append(data)
            while customer_L and n < M and customer_L[0][0] <= time:
                data = list(customer_L.popleft())
                data[0] = time + t
                ans.append(data)
                n += 1
            ferry[1] = "right"
            ferry[0] = time + t
        else: # "right"
            ferry[0] = max(ferry[0],customer_L[0][0]) + t
            n = 1
            data = list(customer_L.popleft())
            time = max(data[0],ferry[0])
            data[0] = time + t
            ans.append(data)
            while customer_L and n < M and customer_L[0][0] <= time:
                data = list(customer_L.popleft())
                data[0] = time + t
                ans.append(data)
                n += 1
            ferry[1] = "left"
            ferry[0] = time + t
    elif customer_R and customer_L and customer_R[0][0] < customer_L[0][0]:
        if ferry[1] == "right":
            n = 1
            data = list(customer_R.popleft())
            time = max(data[0],ferry[0])
            data[0] = time + t
            ans.append(data)
            while customer_R and n < M and customer_R[0][0] <= time:
                data = list(customer_R.popleft())
                data[0] = time + t
                ans.append(data)
                n += 1
            ferry[1] = "left"
            ferry[0] = time + t
        else: # "left"
            ferry[0] = max(ferry[0],customer_R[0][0]) + t # 갔을 때의 시간
            n = 1
            data = list(customer_R.popleft())
            time = max(data[0],ferry[0])
            data[0] = time + t
            ans.append(data)
            while customer_R and n < M and customer_R[0][0] <= time:
                data = list(customer_R.popleft())
                data[0] = time + t
                ans.append(data)
                n += 1
            ferry[1] = "right"
            ferry[0] = time + t
    elif customer_R and customer_L:
        if ferry[1] == "left":
            n = 1
            data = list(customer_L.popleft())
            time = max(data[0],ferry[0])
            data[0] = time + t
            ans.append(data)
            while customer_L and n < M and customer_L[0][0] <= time:
                data = list(customer_L.popleft())
                data[0] = time + t
                ans.append(data)
                n += 1
            ferry[1] = "right"
            ferry[0] = time + t
        else: # "right"
            n = 1
            data = list(customer_L.popleft())
            time = max(data[0],ferry[0])
            data[0] = time + t
            ans.append(data)
            while customer_L and n < M and customer_L[0][0] <= time:
                data = list(customer_L.popleft())
                data[0] = time + t
                ans.append(data)
                n += 1
            ferry[1] = "left"
            ferry[0] = time + t
    elif customer_L:
        if ferry[1] == "left":
            n = 1
            data = list(customer_L.popleft())
            time = max(data[0],ferry[0])
            data[0] = time + t
            ans.append(data)
            while customer_L and n < M and customer_L[0][0] <= time:
                data = list(customer_L.popleft())
                data[0] = time + t
                ans.append(data)
                n += 1
            ferry[1] = "right"
            ferry[0] = time + t
        else: # "right"
            ferry[0] = max(ferry[0],customer_L[0][0]) + t
            n = 1
            data = list(customer_L.popleft())
            time = max(data[0],ferry[0])
            data[0] = time + t
            ans.append(data)
            while customer_L and n < M and customer_L[0][0] <= time:
                data = list(customer_L.popleft())
                data[0] = time + t
                ans.append(data)
                n += 1
            ferry[1] = "left"
            ferry[0] = time + t
    else:
        if ferry[1] == "left":
            ferry[0] = max(ferry[0],customer_R[0][0]) + t
            n = 1
            data = list(customer_R.popleft())
            time = max(data[0],ferry[0])
            data[0] = time + t
            ans.append(data)
            while customer_R and n < M and customer_R[0][0] <= time:
                data = list(customer_R.popleft())
                data[0] = time + t
                ans.append(data)
                n += 1
            ferry[1] = "right"
            ferry[0] = time + t
        else: # "right"
            n = 1
            data = list(customer_R.popleft())
            time = max(data[0],ferry[0])
            data[0] = time + t
            ans.append(data)
            while customer_R and n < M and customer_R[0][0] <= time:
                data = list(customer_R.popleft())
                data[0] = time + t
                ans.append(data)
                n += 1
            ferry[1] = "left"
            ferry[0] = time + t
ans.sort(key = lambda x : x[2])
print(ans)
