#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../")

import unittest
from numEx.num_hw import *


class TestCalFunc(unittest.TestCase):
    def test_Cal_1(self):
        self.assertTrue(isinstance(calendar(2012, 6, 3), type(0)))  # 返回值是否正确
        self.assertEqual(calendar(2013, 2, 29), 'Parameter Error.')

    def test_Cal_2(self):
        self.assertEqual(calendar(2012, 3, 6), 66)

        
if __name__ == '__main__':
    unittest.main()