
from timewrap import cal_time


li = [2, 4, 6, 7, 9, 10, 33, 66, 78, 99]


@cal_time
def bin_search(l, val):
    low = 0
    high = len(li) - 1

    while low <= high:
        mid = (low + high) // 2
        if li[mid] == val:
            return mid
        elif li[mid] < val:
            low = mid + 1
        else:
            high = mid - 1

    return -1


li = list(range(0, 20000))


index_addr = bin_search(li, 100)
print(index_addr)


@cal_time
def sys_search(li, val):
    try:
        return li.index(val)
    except:
        return -1


index_addr = sys_search(li, 100)
print(index_addr)
