
def bubble_sort(alist):

    n = len(alist)

    for k in range(n - 1):
        count = True
        for i in range(n - 1 - k):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count == False
        if count == True:
            break

    return alist


alist = [3, 6, 8, 1, 66, 22, 44, 71, 25, 49, 18]


def main():
    print(bubble_sort(alist))


if __name__ == '__main__':
    main()
