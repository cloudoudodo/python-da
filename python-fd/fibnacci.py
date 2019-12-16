
# 递归求第n个斐波那契数
from timewrap import cal_time


# @cal_time
def fibnacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibnacci(n - 1) + fibnacci(n - 2)


# fibnacci(10)

@cal_time
def fib(n):
    return fibnacci(n)


@cal_time
def fib2(n):
    l = [1, 1]
    for i in range(2, n + 1):
        l.append(l[-1] + l[-2])
    return l[n]


# print(fib2(100))
@cal_time
def fib3(n):
    a = 1
    b = 1
    c = 0
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c

        return c


print(fib3(100))


# 递归求和 1--100
# def fn(n):
#     if n == 1:
#         return 1
#     else:
#         sum_num = fn(n - 1) + n
#         return sum_num


# print(fn(100))

# 递归求一个数的阶乘
# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac(n - 1)


# print(fac(5))
