# 比较运算符

# i = 1
# j = 1
# x = 2
# print(i == j)  # True
# print(i == x)  # False
# print(i > x)  # False
# print(i != x)  # True

# i = 1
# j = '1'
# print(i == j)  # False
# print(i != j)  # True
# x = '1'
# print(j == x)  # True
#
# # 从上面可以看出，字符串和数字比较大小，字符串不会隐式类型转换

# 字符串比较大小

x = "a"
y = "b"
print(x > y)  # False
# 字符串的比较本质上是 ASCII 码的比较
# a 的 ASCII 码为 97，b 的 ASCII 码为 98

# ASCII
# 在ASCII码表中 A 其对应的数字是 65
# a对应的数字是 97  b 98   c 99

i = "ab"
j = "ac"
print(i > j)  # False
# 第一个 `a` 相等，比较顺位比较第二个字符的大小
# 'b' < 'c'，所以 i < j

i = "cb"
j = "aa"
print(i > j)  # True
# 'c' > 'a'，所以 i > j，不用再比较各自的第二个字符了
