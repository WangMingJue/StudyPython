# 题目：将一个列表的数据复制到另一个列表中。
#
# 程序分析：使用列表[:]。

# 最简单的做法
a = [1, 2, 3]
b = a[:]
print(b)

# 进行复制验证，原理是如果没有复制的话，修改第二个列表，原列表的值也会被修改
b[2] = 5
print(a)
print(b)

# 使用copy库完成, 推荐
import copy

a = [1, 5, 9]
b = copy.copy(a)
print(b)

b[2] = 5
print(a)
print(b)
