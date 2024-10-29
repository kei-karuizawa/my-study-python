# 算数运算

first_number = 1
second_number = 2
print(first_number + second_number)  # 3
print(first_number - second_number)  # -1
print(first_number * second_number)  # 2

print(first_number / second_number)  # 0.5，与其他编程语言有所区别，整数相除返回浮点数
print(first_number // second_number)  # 0，Python 的特性，地板除，整数相除返回整数，符合一般编程语言思路
print(first_number % second_number)  # 1，取余（模）运算

first_number = 1.5
second_number = 2
print(first_number + second_number)  # 3.5
print(first_number - second_number)  # -0.5
print(first_number * second_number)  # 3.0
print(first_number / second_number)  # 0.75
print(first_number // second_number)  # 0.0

first_number = 1.5
second_number = 2.0
print(first_number + second_number)  # 3.5
print(first_number - second_number)  # -0.5
print(first_number * second_number)  # 3.0
print(first_number / second_number)  # 0.75
print(first_number // second_number)  # 0.0

s1 = "hello"
s2 = "world"

# 字符串与字符串相加运算，其实是两个字符串拼接
print(s1 + s2)  # helloworld
# 字符串与字符串之间不可以相减
# 字符串与字符串之间不可以相乘
# 字符串与字符串之间不可以相除

# 字符串可以和整数相乘
# 表示字符串的重复
s = 'i'
print(s * 10)  # iiiiiiiiii，打印了 10 个 i

s = 't'
print(s * True)  # t
print(s * False)  # ''，空字符串
