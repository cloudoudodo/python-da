
def select_sort(alist):
    n = len(alist)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if alist[min_index] > alist[j]:
                min_index = j

        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


alist = [7, 5, 3, 6, 44, 22, 99, 11]

print(select_sort(alist))
