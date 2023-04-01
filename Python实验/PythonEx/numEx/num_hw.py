#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os


# 题目九：两地之间距离计算

# 计算两点p1, p2之间的距离
# p1：（纬度、经度）
# p2: （纬度、经度）
def sphere_distance(p1, p2):
    import math

    def hav(theta: float) -> float:  # 弧度的hav值
        return (1 - math.cos(theta)) / 2

    def toRad(theta: float) -> float:  # 角度转弧度
        return theta * math.pi / 180

    R = 6371  # 地球半径
    lat1, lon1 = p1
    lat2, lon2 = p2
    if lat1 > 90 or lat1 < 0 or lat2 > 90 or lat2 < 0 or lon1 > 180 or lon1 < 0 or lon2 > 180 or lon2 < 0:
        return "Parameter Error."
    lat1, lon1, lat2, lon2 = map(toRad, [lat1, lon1, lat2, lon2])
    d = 2 * R * math.asin(math.sqrt(hav(lat2 - lat1) + math.cos(lat1) * math.cos(lat2) * hav(lon2 - lon1)))
    return round(d, 2)


# 题目十：计算Fibonacci 序列的值
# Fibonacci是1，1, 2，3，5, 8，13.....
# n1 = 1, n2 =2, n3 = n1+n2, n4 = n3+n2
def fibonacci_recursion(number):
    if isinstance(number, int) and number > 0:
        if number == 1 or number == 2:
            return 1
        else:
            return fibonacci_recursion(number - 1) + fibonacci_recursion(number - 2)
    else:
        return "Parameter Error."


def fibonacci_loop(number):
    if isinstance(number, int) and number > 0:
        if number == 1 or number == 2:
            return 1
        else:
            a = 1
            b = 1
            for i in range(3, number + 1):
                a, b = b, a + b
            return b
    else:
        return "Parameter Error."


# 题目一：水仙花数
def narcissistic_number():
    Nar_num = []
    for i in range(100, 1000):
        a = i // 100
        b = i // 10 % 10
        c = i % 10
        if a ** 3 + b ** 3 + c ** 3 == i:
            Nar_num.append(i)
    return Nar_num


# 题目二：完美数
def perfect_number(limit=1000):
    if limit <= 0:
        return "Parameter Error."
    elif limit is None:
        return []
    Per_list = []
    for i in range(1, limit + 1):
        Num = 0
        for j in range(1, i):
            if i % j == 0:
                Num += j
        if Num == i:
            Per_list.append(i)
    return Per_list


# 题目三：百钱百鸡
def buy_chicken():
    result = []
    for i in range(0, 21):
        for j in range(0, 34):
            k = 100 - i - j
            if 5 * i + 3 * j + k / 3 == 100:
                result.append([i, j, k])
    return result


# 题目四
# 最大公约数
def gcd(x, y):
    if x <= 0 or y <= 0:
        return "Parameter Error."
    if not isinstance(x, int) or not isinstance(y, int):
        return "Parameter Error."
    if x < y:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return int(x)


# 最小公倍数
def lcm(x, y):
    if x <= 0 or y <= 0:
        return "Parameter Error."
    if not isinstance(x, int) or not isinstance(y, int):
        return "Parameter Error."
    return int(x * y / gcd(x, y))


# 题目五：回文数
def is_palindrome_number(num):
    if num < 0:
        return False
    elif num == 0:
        return True
    else:
        num = str(num)
        if num == num[::-1]:
            return True
        else:
            return False


# 题目六：素数
def is_prime_num(num):
    if not isinstance(num, int):
        return "Parameter Error."
    if num < 1:
        return "Parameter Error."
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# 题目七：约瑟夫环
def jose_prob(n, m):
    if not isinstance(n, int) or not isinstance(m, int):
        return "Parameter Error."
    Total = [True] * m
    count = 1
    while Total.count(True) > n:
        for i in range(m):
            if Total[i]:
                if count == 9:
                    Total[i] = False
                    count = 1
                else:
                    count += 1
    # 计算初始位置，1代表基督徒，0代表非基督徒
    result = []
    for i in range(m):
        if Total[i]:
            result.append(1)
        else:
            result.append(0)
    return result


# 题目八：万年历
def calendar(year, month, day):
    if year < 0 or month < 1 or month > 12 or day < 1 or day > 31:
        return "Parameter Error."
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if day > 29:
                return "Parameter Error."
        else:
            if day > 28:
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


if __name__ == '__main__':
    calendar(2012, 7, 12)
