# 数据类型转换

i = 0
print(type(i))  # <class 'int'>
j = 1.8
print(type(j))  # <class 'float'>
x = ""
print(type(x))  # <class 'str'>
y = False
print(type(y))  # <class 'bool'>

i = 0
# 整数类型可以转换成浮点数
ii = float(i)
print(ii)  # 0.0
print(type(ii))  # <class 'float'>

# 整数类型可以转换成字符串
si = str(i)
print(si)  # 0
print(type(si))  # <class 'str'>

# 整数类型可以转换成布尔值
# 1 可以转换成True、 0 可以转换成False
bi = bool(i)
print(bi)  # False
print(type(bi))  # <class 'bool'>

# 浮点数可以转换成整数
j = 1.8
ij = int(j)
print(ij)  # 1，浮点数转整数去掉小数点后的部分
print(type(ij))  # <class 'int'>

# 浮点数可以转字符串
sj = str(j)
print(sj)  # 1.8
print(type(sj))  # <class 'str'>

# 浮点数可以转布尔值
# 非 0 的数字类型，转换成布尔值的时候就会变成 `True`
bj = bool(j)
print(bj)  # True
print(type(bj))  # <class 'bool'>

# 字符串如果想要转换成整型或浮点数，那么它必须看起来就像是一个数字才可以
x = ''
# ix = int(x)  # 会报错
# fx = float(x)  # 会报错
y = 1
z = 2.0
# 字符串转整型
iy = int(y)
print(iy)  # 1
print(type(iy))  # <class 'int'>
# 字符串转浮点数
fz = float(z)
print(fz)  # 2.0
print(type(z))  # <class 'float'>

# 字符串转换成布尔值时，空值为 `False`，有值的时候为 `True`
bx = bool(x)
print(bx)  # False
print(type(bx))  # <class 'bool'>



y = False
# 布尔值转整型
iy = int(y)
print(iy)  # 0
print(type(iy))  # <class 'int'>

# 布尔值转浮点数
fy = float(y)
print(fy)  # 0.0
print(type(fy))  # <class 'float'>

# 所以：布尔值的参与数值类型转换时，是 0 和 1 参与转换

# 布尔值转字符串
# 布尔值转字符串时，最终转换成 `'True'` 或者 `'False'` 字符串
sy = str(y)
print(sy)  # False
print(type(sy))  # <class 'str'>
