

import random
# 时间复杂度 n*logn


def quick_sort(li, left, right):
    if left < right:  # 待排序的区域至少有两个元素
        mid = random_partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]

    li[left] = tmp
    return left


def random_partition(li, left, right):
    i = random.randint(left, right)
    li[i], li[left] = li[left], li[i]
    return partition(li, left, right)


def quick_sort2(li):
    if len(li) < 2:
        return li
    tmp = li[0]
    left = [v for v in li[1:] if v <= tmp]
    right = [v for v in li[1:] if v > tmp]
    left = quick_sort2(left)
    right = quick_sort2(right)
    return left + [tmp] + right


li = list(range(100))
random.shuffle(li)
print(li)
# quick_sort(li, 0, len(li) - 1)
quick_sort2(li)
print(li)
