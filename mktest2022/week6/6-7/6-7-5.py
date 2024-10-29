# 字典的添加、修改和删除

my_dict = {
    1: 'a',
    2: 'b',
    3: 'c'
}

# 添加操作
my_dict.update({4: 'd'})
print(my_dict)  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# 更新值
my_dict[1] = "aaaaa"
print(my_dict)  # {1: 'aaaaa', 2: 'b', 3: 'c', 4: 'd'}

# 字典的删除操作
my_dict.pop(2)
print(my_dict)  # {1: 'aaaaa', 3: 'c', 4: 'd'}
