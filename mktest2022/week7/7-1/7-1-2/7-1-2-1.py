# 闭包

def func1():
    print('函数 1 执行')
    return func2


def func2():
    print('函数 2 执行')
    return 2


r = func2()  # 函数 2 执行
print(r)  # 2

r2 = func1() # 函数 1 执行
print(r2)  # <function func2 at 0x104a54790>
print(r2())
# 函数 2 执行
# 2