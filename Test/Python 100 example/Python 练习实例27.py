# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
#
# 程序分析：无。


def output(s, li):
    if li == 0:
        return
    print(s[li - 1])
    output(s, li - 1)


s = input('Input a string:')
li = len(s)
output(s, li)
