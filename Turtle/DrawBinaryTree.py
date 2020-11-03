from turtle import *


def draw(strength):
    if strength > 0:
        fd(strength)
        rt(20)  # 右转20°
        draw(strength - 5)  # 每一节树枝比前一节短5

        lt(40)  # 之前右转了20°，所以这里要左转40°。
        draw(strength - 5)
        if (strength < 25):
            pencolor("green")  # 如果树枝的长度小于25，那么就设置画笔的颜色为绿色
        rt(20)
        backward(strength)  # 放回
        pencolor("black")


if __name__ == '__main__':
    tree_length = 36  # 设置树的长度
    penup()
    goto(-50, -100)  # 向下移动画笔
    pendown()
    left(90)  # 开始画笔的方向为朝右，转到向上
    draw(tree_length)
    exitonclick()  # 设置画完后不立即结束程序
