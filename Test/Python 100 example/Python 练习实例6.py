# 题目：斐波那契数列。
#
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
#
# 在数学上，费波那契数列是以递归的方法来定义：
# F0 = 0     (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)


# 普通方法
def method_1(index):
    a, b = 1, 1
    for i in range(index - 1):
        a, b = b, a + b
    return a


# 使用递归
def method_2(index):
    if index == 1 or index == 2:
        return 1
    return method_2(index - 1) + method_2(index - 2)


# 输出前 n 个斐波那契数列
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


if __name__ == '__main__':
    print("第一种方法输出了第10个斐波那契数列，结果为:{}".format(method_1(10)))
    print("第二种方法输出了第10个斐波那契数列，结果为:{}".format(method_1(10)))
    print("输出前10个斐波那契数列，结果为:{}".format(fib(10)))
