# -*- coding: utf-8 -*-
"""
计算 Fibonacci 列的值(模块: numEx，所在文件名num hw.py，Level:
利用Python实现Fibonacci 序列值的计算。实现两个函数:
(1)递归版本的 Fibonacci 序列值计算
函数原型: deffibonacci recursion(number)
参数number: Fibonacci序列的第number 项，number 为大于0的整数
返回值:如果参数合规，则返回 Fibonacci 序列的第 number 项的值;如果参数不合规,返回错误“Parameter Error.”
(2)循环版本的 Fibonacci 序列值计算
函数原型: def fibonacci loop(number)
参数 number: Fibonacci 序列的第 number 项，number 为大于0的整数
返回值:如果参数合规，则返回 Fibonacci 序列的第 number 项的值:如果参数不合规返回错误“Parameter Error.。
问题:
(1)查看 fibonacci loop(36)与 fbonacci recursion(36)的运行时间，哪个运行快?
(2) fibonacci recursion 版本支持的最大输入是多少?最大值如何更改?
"""


def fibonacci_recursion(number: int) -> int or str:
    if isinstance(number, int) and number > 0:
        if number == 1 or number == 2:
            return 1
        else:
            return fibonacci_recursion(number - 1) + fibonacci_recursion(number - 2)
    else:
        return "Parameter Error"


def fibonacci_loop(number: int) -> int or str:
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
        return "Parameter Error"


if __name__ == '__main__':
    # 统计时间
    import time
    """
    fib1(36) time:  3.0999972820281982
    fib2(36) time:  0.0
    """
    start = time.time()
    fibonacci_recursion(36)
    end = time.time()
    print("fib1(36) time: ", end - start)
    start = time.time()
    fibonacci_loop(36)
    end = time.time()
    print("fib2(36) time: ", end - start)

    """
    RecursionError: maximum recursion depth exceeded while calling a Python object
    最大值为1000
    """
    # fibonacci_recursion(1000)
    # 更改maximum recursion depth
    # import sys
    # sys.setrecursionlimit(10000)
    # fibonacci_recursion(1000)
