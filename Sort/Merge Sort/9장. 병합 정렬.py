num = [6, 7, 2, 1, 8, 5, 4, 3]

def merge_sort(num):
    def sort(s, e):
        if e - s <= 1:
            return
        mid = (s + e) // 2
        sort(s, mid)
        sort(mid, e)
        merge(s, mid, e)

    def merge(s, mid, e):
        temp = []
        l = s
        m = mid
        while l < mid and m < e:
            if num[l] > num[m]:
                temp.append(num[m])
                m += 1
            else:
                temp.append(num[l])
                l += 1

        while  l < mid:
            temp.append(num[l])
            l += 1
        while  m < e:
            temp.append(num[m])
            m += 1
        for i in range(s, e):
            num[i] = temp[i - s]
    return sort(0, len(num))

merge_sort(num)
print(num)
