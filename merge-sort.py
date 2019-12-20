import random


def merge2list(li1, li2):  # 两个有序列表合并
    li = []
    i = 0
    j = 0
    while i < len(li1) and j < len(li2):
        if li1[i] < li2[j]:
            li.append(li1[i])
            i += 1
        else:
            li.applend(li2[j])
            j += 1

    while i < len(li1):
        li.append(li1[i])
        i += 1
    while j < len(li2):
        li.append(li2[j])
        j += 1
    return li


def merge(li, low, mid, high):  # 一次归并
    #
    i = low
    j = mid + 1
    li_tmp = []
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            li_tmp.append(li[i])
            i += 1
        else:
            li_tmp.append(li[j])
            j += 1

    while i <= mid:
        li_tmp.append(li[i])
        i += 1

    while j <= high:
        li_tmp.append(li[j])
        j += 1

    for i in range(low, high + 1):
        li[i] = li_tmp[i - low]

    #li[low:high+1] = li_tmp


def mergeSort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort(li, low, mid)
        mergeSort(li, mid + 1, high)
        merge(li, low, mid, high)


li = list(range(10))
random.shuffle(li)
print(li)
mergeSort(li, 0, len(li) - 1)
print(li)
