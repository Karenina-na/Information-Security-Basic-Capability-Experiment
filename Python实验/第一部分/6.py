# -*- coding: utf-8 -*-
"""
素数指的是除了 1和它本身以外没有其他因数的数。设计函数验证一个数是否为素数。函数原型: defis prime num(n)
参数 n: 正整数，输入待测试的数字。负数、小数归为异常参数
返回值:布尔型，如果这个数是回文数返回 True，否则返回 False。如果参数异常，返回错误“Parameter Error.
"""


def is_prime_num(n: int) -> bool or str:
    if not isinstance(n, int):
        return "Parameter Error"
    if n < 1:
        return "Parameter Error"
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(is_prime_num(1))
    print(is_prime_num(2))
    print(is_prime_num(3))
    print(is_prime_num(4))
