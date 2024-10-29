# 函数的返回值

def add(x, y):
    r = x + y
    print(22222)
    return r
    # return 之后的语句不会执行
    print(11111)


add(1, 2)

# 接收函数返回值
result = add(2, 3)
print(result)  # 5