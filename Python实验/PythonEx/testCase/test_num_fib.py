#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../")

import unittest
from numEx.num_hw import *


# 单元测试
class TestFibFunc(unittest.TestCase):

    # 题目：Fibonacci数列
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci_recursion(0), 'Parameter Error.')
        self.assertEqual(fibonacci_loop(0), 'Parameter Error.')

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci_recursion(30), 832040)

    def test_fibonacci_3(self):
        self.assertEqual(fibonacci_loop(30), 832040)


if __name__ == '__main__':
    unittest.main()