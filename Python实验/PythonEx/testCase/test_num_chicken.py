#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../")

import unittest
from numEx.num_hw import *


# 如何判断运行时间
class TestChickenFunc(unittest.TestCase):
    def test_Chicken_1(self):
        self.assertTrue(isinstance(buy_chicken(), type([])))  # 返回值是否正确

    def test_Chicken_2(self):
        self.assertEqual(buy_chicken(), [[0, 25, 75], [4, 18, 78], [8, 11, 81], [12, 4, 84]])


if __name__ == '__main__':
    unittest.main()
