# -*- coding: utf-8 -*-
"""
给出一个年月日，计算这一天是那一年的第几天。函数原型: def calendar(year,month,day)
参数 year:四位正整数，年，如2000。
参数month:1-12的正整数，月
参数 day:1-31的正整数，日
返回值:正整数，表示这一天是那一年的第几天。如果参数异常，返回错误“Parameter
Error.%
"""


def calendar(year, month, day):
    if year < 0 or month < 1 or month > 12 or day < 1 or day > 31:
        return "Parameter Error."
    days = 0
    for i in range(1, month):
        if i == 2:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                # 闰年
                days += 29
            else:
                days += 28
        elif i in [1, 3, 5, 7, 8, 10, 12]:
            # 大月
            days += 31
        else:
            # 小月
            days += 30
    days += day
    return days


if __name__ == "__main__":
    print(calendar(2000, 2, 29))
