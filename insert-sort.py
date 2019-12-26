def insert_sort(alist):

    n = len(alist)

    for j in range(1, n):
        i = j

        while i > 0:
            if alist[i] < alist[i - 1]:  # 交换两个数的位置
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            else:
                break

            i -= 1

    return alist


alist = [3, 6, 8, 1, 66, 22, 44, 71, 25, 49, 18]


def insert_sort2(li):
    for i in range(1, len(li)):
        tmp = li[i]  # 摸到的牌存起来
        j = i - 1    # 等待被比较的牌
        while j >= 0 and li[j] > tmp:  # 只要往后挪就循环2个条件都得满足
            # 如果j =-1 或者li[j]小了，停止挪动
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp  # j在循环结束的时候要么是-1，要么是个比tmp小的值


def main():
    print(alist)
    insert_sort2(alist)
    print(alist)


if __name__ == '__main__':
    main()
