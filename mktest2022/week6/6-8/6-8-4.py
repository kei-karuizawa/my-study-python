# 函数的返回值

def my_function():
    i = 1
    j = 2
    return i, j, 3, 4, 5


print(my_function())  # (1, 2, 3, 4, 5)
print(type(my_function()))  # <class 'tuple'>
result = my_function()
print(result)  # (1, 2, 3, 4, 5)
(a, b, c, d, e) = result
print(a, b, c, d, e)  # 1 2 3 4 5

# 若接收函数返回值的变量个数和函数实际返回的变量个数不一致，会报错
(h, i, j, k) = result
print(h, i, j, k)  # 报错
