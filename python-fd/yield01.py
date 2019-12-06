def myyield():
    yield 2
    yield 3
    yield 5


for x in myyield():
    print(x)

gen = myyield()

it = iter(gen)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
