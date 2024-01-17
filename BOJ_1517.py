import sys
input = sys.stdin.readline
cnt = 0 # 최종적인 답

def merge_sort(list1,start1,list2,start2): # 병합하는 함수
    global cnt
    n1 = len(list1)
    n2 = len(list2)
    merge_list = []
    while start1 < n1 and start2 < n2:
        if list1[start1] <= list2[start2]:
            merge_list.append(list1[start1])
            start1 += 1
        else:
            cnt += n1 - start1
            merge_list.append(list2[start2])
            start2 += 1

    while start1 < n1:
        merge_list.append(list1[start1])
        start1 += 1
    while start2 < n2:
        merge_list.append(list2[start2])
        start2 += 1

    return merge_list # 최종적으로 병합한 리스트 반환

N = int(input())
num = list(map(int,input().split()))
merge_list = [[x] for x in num]
n = N

while n != 1:
    merge_list1 = []
    for idx in range(0,n,2):
        if idx + 1 < n:
            merge_list1.append(merge_sort(merge_list[idx],0,merge_list[idx + 1],0))
        else:
            merge_list1.append(merge_list[idx])
    merge_list = merge_list1
    n = len(merge_list)

print(cnt)
