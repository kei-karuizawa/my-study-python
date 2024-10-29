# yield 关键字

def func1():
    return "自信的生命最美丽"
    print("含泪播种的人必须能含笑收获")


# r1 = func1()
# print(r1)  # 自信的生命最美丽
# return 语句后面的内容不会被执行

def func2():
    print("勤于反省，才有不断进步的可能")
    # yield返回的是一个生产器对象
    yield "一个人，想要优秀，你必须要敢于挑战"
    print("有志者事竟成，苦心人天不负")
    yield "第二个yield"
    print("第二个yield后边的print")


r2 = func2()
# print(r2)  # <generator object func2 at 0x10121e120>

# r2.__next__()  # 勤于反省，才有不断进步的可能
# r2.__next__()  # 有志者事竟成，苦心人天不负
# r2.__next__()  # 报错；StopIteration

# 生成器对象可以用 for 循环来迭代
# for i in r2:
#     print(i)


# 勤于反省，才有不断进步的可能
# 一个人，想要优秀，你必须要敢于挑战
# 有志者事竟成，苦心人天不负
# 第二个yield
# 第二个yield后边的print

count = 1
for i in r2:
    # 这里打印的 i 是生成器对象 yield 后边的那个返回值
    print(i)
    count += 1
    print("for 循环调用生成器的 {} 打印".format(count))
    print("*" * 20)


# 勤于反省，才有不断进步的可能
# 一个人，想要优秀，你必须要敢于挑战
# for 循环调用生成器的 2 打印
# ********************
# 有志者事竟成，苦心人天不负
# 第二个yield
# for 循环调用生成器的 3 打印
# ********************
# 第二个yield后边的print