#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../")

import unittest
from numEx.num_hw import *


class TestPrimeFunc(unittest.TestCase):
    def test_PriNum_1(self):
        self.assertTrue(isinstance(is_prime_num(5.8), type('')))
        self.assertEqual(is_prime_num(1453.6), 'Parameter Error.')
        self.assertEqual(is_prime_num(-1453), 'Parameter Error.')
        self.assertTrue(isinstance(is_prime_num(5), type(True)))  # 返回值是否正确
        self.assertEqual(is_prime_num(1453), True)
        self.assertEqual(is_prime_num(1024), False)


if __name__ == '__main__':
    unittest.main()