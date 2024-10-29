# 装饰器

def runtime(func):
    def warpper():
        print(1)
        return func()
    return warpper


def my_func1():
    print('函数 1 执行')
    return 2


@runtime
def my_func2():
    print('函数 2 执行')
    return 4


r = my_func1()  # 函数 1 执行
print(r)  # 2

r2 = my_func2()
# 1
# 函数 2 执行

print(r2)  # 4
