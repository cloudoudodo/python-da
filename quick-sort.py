


def quick_sort(alist, start, end):
    if start >= end:
        return

    mid = alist[start]
    low = start
    high = end

    while low < high:
        while alist[high] > mid and low < high:
            high -= 1

        alist[low] = alist[high]

        while alist[low] < mid and low < high:
            low += 1

        alist[high] = alist[low]

    alist[low] = mid

    quick_sort(alist, start, low - 1)

    quick_sort(alist, low + 1, end)


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist, 0, len(alist) - 1)
    print(alist)

