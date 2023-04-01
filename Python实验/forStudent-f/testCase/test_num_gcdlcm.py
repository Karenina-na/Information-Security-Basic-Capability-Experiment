#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../")

import unittest
from numEx.num_hw import *


class TestGcdFunc(unittest.TestCase):
    def test_gcd_1(self):
        self.assertTrue(isinstance(gcd(1, 2), type(0)))  # 返回值是否正确
        self.assertEqual(gcd(-2, 7428), 'Parameter Error.')

    def test_gcd_2(self):
        self.assertEqual(gcd(490, 2002), 14)

    def test_lcm_1(self):
        self.assertTrue(isinstance(lcm(1, 2), type(0)))
        self.assertEqual(lcm(-2, 7428), 'Parameter Error.')

    def test_lcm_2(self):
        self.assertEqual(lcm(490, 2002), 70070)


        
if __name__ == '__main__':
    unittest.main()
