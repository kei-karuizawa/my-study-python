# 循环

i = 1
while i <= 10:
    print('while 的条件满足则执行这里的语句')
    i += 1  # 跳出循环语句的条件

# 注意：while 循环比较有跳出循环的语句，否则会陷入死循环

# 分别打印出字符串中的每个字符
s = 'abcde'
for i in s:
    print(i)

# 打印数组的每一项
array = ['a', 'b', 'c', 'd', 'e']
for i in array:
    print(i)

# 打印元组的每一项
tuple1 = ('a', 'b', 'c', 'd', 'e')
for i in tuple1:
    print(i)

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# 打印字典的所有 key
for i in dict.keys():
    print(i)

# 打印字典的所有 value
for i in dict.values():
    print(i)

# 打印字典的所有 key 和 value
for key, value in dict.items():
    print(key, value)
