def insert_sort(alist):

    n = len(alist)

    for j in range(1, n):
        i = j

        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            else:
                break

            i -= 1

    return alist


alist = [3, 6, 8, 1, 66, 22, 44, 71, 25, 49, 18]


def main():
    print(insert_sort(alist))


if __name__ == '__main__':
    main()
