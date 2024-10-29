# 字符串格式化

# % 操作符，已经落伍了
# 多个变量用元组包裹
i = 20.5
j = 'python'
z = 5

print('我花费 %.1f 元买了本 %s 书，学习了 %d 个小时' % (i, j, z))
# 我花费 20.5 元买了本 python 书，学习了 5 个小时

# format 方法格式化
print('我花费 {} 元买了本 {} 书，学习了 {} 个小时'.format(i, j, z))
# 我花费 20.5 元买了本 python 书，学习了 5 个小时

# format 也可以按照对应的名字进行格式化
print('我花费 {price} 元买了本 {name} 书，学习了 {hours} 个小时'.format(price=i, name=j, hours=z))
# 我花费 20.5 元买了本 python 书，学习了 5 个小时

# format 也可以按照对应变量序号进行格式化
print('我花费 {0} 元买了本 {1} 书，学习了 {2} 个小时'.format(i, j, z))
# 我花费 20.5 元买了本 python 书，学习了 5 个小时

# format 的格式化符是在 {} 里加上 :x
print('我花费 {price:.2f} 元买了本 {name} 书，学习了 {hours} 个小时'.format(price=i, name=j, hours=z))
# 我花费 20.50 元买了本 python 书，学习了 5 个小时

# 不仅如此，format 的 {} 里面还可以加更复杂的东西
print('我花费 {info[0]} 元买了本 {info[1]} 书，学习了 {info[2]} 个小时'.format(info=(i, j, z)))
# 我花费 20.5 元买了本 python 书，学习了 5 个小时
# 但这会带来一些安全隐患，可能通过外部程序注入一些非法东西

# 模版字符串
print(f'我花费 {i} 元买了本 {j} 书，学习了 {z} 个小时')
# 我花费 20.5 元买了本 python 书，学习了 5 个小时
