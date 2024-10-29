# 函数的参数

# 带参数的函数声明
def add(x, y):
    print(x + y)


# 函数调用
add(1, 2)  # 3


def add(x, y, z=0):
    print(x + y + z)


# 调用时可以不指定默认参数的实际值，此时取的是参数的默认值（0）
add(2, 2)  # 4

# 也可以指定默认参数的值
add(3, 3, 1)  # 7

# 调用函数时可以带上参数的名字，这样可以不必按照函数定义时的参数列表顺序
add(x=4, y=4, z=2)  # 10
add(z=2, y=4, x=4)  # 10


def add(*params):
    print(params)
    print(type(params))
    isum = 0
    for i in params:
        isum += i
    print(isum)


add(1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)
# <class 'tuple'>
# 15

add(1, 2)


# (1, 2)
# <class 'tuple'>
# 3

def my_function(**params):
    print(params)
    print(type(params))
    for k, v in params.items():
        print(k, v)


my_function(x=1, y=2, z=3)
# {'x': 1, 'y': 2, 'z': 3}
# <class 'dict'>
# x 1
# y 2
# z 3

my_function(h=1, w=2)
# {'h': 1, 'w': 2}
# <class 'dict'>
# h 1
# w 2