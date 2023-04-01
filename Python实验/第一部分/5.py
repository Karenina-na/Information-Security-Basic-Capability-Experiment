# -*- coding: utf-8 -*-
"""
如果一个数反过来与原数相同，那么这就是一个回文数。比如，121 就是一个回文数-121 不是一个回文数。设计函数验证一个数是否为回文数。
函数原型: defis palindrome number(n)
参数 n:输入待测试的数字，可能是正数、负数、整数、浮点数等数值返回值:布尔型，如果这个数是回文数返回 True，否则返回 False
"""


def pal_num(x: int or float) -> bool:
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    print(pal_num(121))
    print(pal_num(-121))
    print(pal_num(0))
    print(pal_num(123))
