#버블 정렬(O(n**2))
num = [7,1,4,3,9,2,6,5,8]
n = len(num)

for i in range(n - 1,-1,-1):
    for j in range(0,i):
        if num[j] > num[j + 1]:
            num[j],num[j + 1] = num[j + 1],num[j]

print(num)

#선택 정렬(O(n**2))
num = [7,1,4,3,9,2,6,5,8]
n = len(num)

for i in range(n):
    minN = num[i]
    for j in range(i + 1,n):
        if num[j] < minN:
            minN = num[j]
            change_point = j
    num[i],num[change_point] = num[change_point],num[i]

print(num)

#삽입 정렬(O(n**2))
num = [7,1,4,3,9,2,6,5,8]
n = len(num)

for i in range(1,n):
    for j in range(i,0,-1):
        if num[j] > num[j - 1]:
            break
        else:
            num[j],num[j - 1] = num[j - 1],num[j]

print(num)

# 퀵 정렬(O(nlogn) or O(n**2))
def quick_sort(start,end,num):
    # 리스트가 한개인 경우
    if start >= end:
        return
    pivot = start
    left,right = start + 1,end

    while left <= right:
        # left는 pivot보다 큰 수 찾기
        while left <= end and num[left] <= num[pivot]:
            left += 1
        # right는 pivot보다 작은 수 찾기
        while right > start and num[right] >= num[pivot]:
            right -= 1
        # 아직 엇갈리지 않았다면
        if left <= right:
            num[left],num[right] = num[right],num[left] # swap
        # 엇갈렸다면
        else:
            num[pivot],num[right] = num[right],num[pivot] # swap
    quick_sort(start,right - 1,num)
    quick_sort(right + 1,end,num)

num = [7,1,4,3,9,2,6,5,8]
n = len(num)

start = 0
end = n - 1
quick_sort(start,end,num)

print(num)

#병합 정렬(O(nlogn))

def merge_sort(list1,start1,list2,start2): # 두 리스트 병합하기
    n1 = len(list1)
    n2 = len(list2)
    merge_list = []
    while start1 < n1 and start2 < n2:
        if list1[start1] < list2[start2]:
            merge_list.append(list1[start1])
            start1 += 1
        else:
            merge_list.append(list2[start2])
            start2 += 1

    if start1 < n1:
        for i in range(start1,n1):
            merge_list.append(list1[i])
    elif start2 < n2:
        for i in range(start2,n2):
            merge_list.append(list2[i])

    return merge_list

num = [7,1,4,3,9,2,6,5,8]
n = len(num)

merge_list = [[x] for x in num]

while len(merge_list) != 1:
    merge_list1 = []
    for idx in range(0,len(merge_list),2): # 2칸씩 건너뛰기 안해서 이상해짐
        if idx + 1 < len(merge_list):
            merge_list1.append(merge_sort(merge_list[idx],0,merge_list[idx + 1],0))
        else:
            merge_list1.append(merge_list[idx])
    merge_list = merge_list1

print(merge_list[0])
