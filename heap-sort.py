
import random
import heapq


def sift(li, low, high):
    # li表示树，low表示树的跟，high表示最后一个节点的位置，标记了树的范围
    tmp = li[low]
    i = low
    j = 2 * i + 1
    # i 指向空位，j表示孩子节点的位置
    while j <= high:  # 第二种情况，空位i是叶子节点
        # 如果存在右孩子且右孩子比左孩子大，j指向右孩子
        if j + 1 <= high and li[j] < li[j + 1]:
            j += 1

        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:  # 循环退出的第一种情况，j位置的值比tmp小，说明两个孩子节点都比tmp小
            break

    li[i] = tmp


def heap_sort(li):
    # 构造堆
    n = len(li)

    for low in range(n // 2 - 1, -1, -1):
        sift(li, low, n - 1)

    print('heap list is  ', li)

    for high in range(n - 1, -1, -1):
        li[0], li[high] = li[high], li[0]  # 退休棋子调整
        sift(li, 0, high - 1)


li = list(range(10))
random.shuffle(li)
print(li)
heap_sort(li)
print(li)

random.shuffle(li)
heapq.heapify(li)
print(li)
