# 闭包与装饰器


def make_power(y):
    def fx(arg):
        return arg ** y
    return fx


pow2 = make_power(2)

print('3**2 = ', pow2(3))

pow3 = make_power(3)

print('3**3 = ', pow3(3))


# 用参数返回响应数学函数的实例
# y = a*x**2 + b*x + c

def make_function(a, b, c):
    def fx(x):
        return a * x**2 + b * x + c
    return fx


fx1 = make_function(4, 5, 6)
print(fx1(2))


# 定义装饰器
def mydeco(fn):
    def fx():
        print('+++++++++++')
        fn()
        print('+++++++++++')
    return fx

# myfunc = mydeco(myfunc)  等同于装饰器


@mydeco
def myfunc():
    print('muyfunc called')


myfunc()
myfunc()
myfunc()
