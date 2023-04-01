# -*- coding: utf-8 -*-
"""
函数原型: def gcd(x,y)，求取最大公约数
函数原型: deflcm(x,)，求取最小公倍数
参数X，y:正整数
返回值:正整数，其中 gcd(xy)返回x 与y的最大公约数，lcm(x,y)求取x与y的最小公倍数。如果参数异常，返回错误“Parameter Errtr.
"""


def gcd(x, y) -> object or int:
    if x <= 0 or y <= 0:
        return "Parameter Error"
    if not isinstance(x, int) or not isinstance(y, int):
        return "Parameter Error"
    if x < y:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x


def lcm(x, y) -> object:
    if x <= 0 or y <= 0:
        return "Parameter Error"
    if not isinstance(x, int) or not isinstance(y, int):
        return "Parameter Error"
    return x * y / gcd(x, y)


if __name__ == "__main__":
    print(gcd(12, 18))
    print(lcm(12, 18))
