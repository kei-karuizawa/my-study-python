# 列表的元素的增加、删除和更新

my_list = [1, 2, 3, 4, 5]

# 列表元素添加
my_list.append(6)
print(my_list)  # [1, 2, 3, 4, 5, 6]

# 列表元素更新
my_list[5] = 7
print(my_list)  # [1, 2, 3, 4, 5, 7]

# 如果访问的序号值超过数组，则会报错
# my_list[8] = 10  # 报错
# print(my_list)

# 列表元素的删除

# 根据元素的值删除
my_list.remove(7)
print(my_list)  # [1, 2, 3, 4, 5]

# 根据元素的序号删除
my_list.pop(3)
print(my_list)  # [1, 2, 3, 5]
