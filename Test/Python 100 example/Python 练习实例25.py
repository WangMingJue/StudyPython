# 题目：求1+2!+3!+...+20!的和。
#
# 程序分析：此程序只是把累加变成了累乘。

# 方法一
n = 0
s = 0
t = 1
for n in range(1, 21):
    t *= n
    s += t
print('1! + 2! + 3! + ... + 20! = %d' % s)


# 方法二
def op(x):
    r = 1
    for i in range(1, x + 1):
        r *= i
    return r


my_list = range(1, 21)
s = sum(map(op, my_list))
print('1! + 2! + 3! + ... + 20! = %d' % s)
