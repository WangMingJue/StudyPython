# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
#
# 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。


# 使用了列表的内置函数
def method_2(my_sort_list):
    my_sort_list.sort()
    return my_sort_list


# 使用了数据结构中的冒泡排序
def method_1(my_list):
    for i in range(len(my_list)):
        for j in range(i, len(my_list)):
            if my_list[i] > my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    return my_list


if __name__ == '__main__':
    my_list = []
    for i in range(3):
        x = int(input('请输入一个数:\n'))
        my_list.append(x)

    print("你输入的列表为:{}".format(my_list))
    print("第一种方法的结果是:{}".format(method_1(my_list)))
    print("第二种方法的结果是:{}".format(method_2(my_list)))
