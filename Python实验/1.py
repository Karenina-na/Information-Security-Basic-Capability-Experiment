# -*- coding: utf-8 -*-
"""
水仙花数(Narcissistic number) 是指一个 3位数，它的每个位上的数字的 3次幂之和等于它本身(例如:13 +53+ 33 =153)。本题要求寻找所有的水仙花数。
函数原型: defnarcissistic number0)
返回值: 返回一个 list，包含了所寻找到的全部水仙花数的数值，要求这些数从小到大排列。每一个数都应当为整形，如[153,370,371]。
"""


def Nar() -> []:
    Nar_num = []
    for i in range(100, 1000):
        a = i // 100
        b = i // 10 % 10
        c = i % 10
        if a ** 3 + b ** 3 + c ** 3 == i:
            Nar_num.append(i)
    return Nar_num


if __name__ == "__main__":
    print(Nar())
