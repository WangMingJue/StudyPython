# 题目：输出指定格式的日期。
#
# 程序分析：使用 datetime 模块。

import datetime

if __name__ == '__main__':
    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%d/%m/%Y'))

    # 创建日期对象
    BirthDate = datetime.date(1941, 1, 5)

    print(BirthDate.strftime('%d/%m/%Y'))

    # 日期算术运算
    BirthNextDay = BirthDate + datetime.timedelta(days=1)

    print(BirthNextDay.strftime('%d/%m/%Y'))

    # 日期替换
    FirstBirthday = BirthDate.replace(year=BirthDate.year + 1)

    print(FirstBirthday.strftime('%d/%m/%Y'))
