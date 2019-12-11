def myyield():
    yield 2
    yield 3
    yield 5


for x in myyield():
    print(x)

# gen = myyield() # gen 绑定一个生成器

# it = iter(gen)  # it 绑定一个迭代器

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


def myodd(x):
    i = 0
    while i < x:
        if i % 2 == 1:
            yield i
        i += 1


for x in myodd(10):
    print(x)


for a in range(1001):
    for b in range(1001):
        for c in range(1001):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print('a: ', a, 'b: ', b, 'c: ', c)
