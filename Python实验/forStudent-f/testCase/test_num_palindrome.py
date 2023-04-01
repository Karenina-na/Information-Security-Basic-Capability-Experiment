#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../")

import unittest
from numEx.num_hw import *


class TestPalFunc(unittest.TestCase):
    def test_PalNum_1(self):
        self.assertTrue(isinstance(is_palindrome_number(8), type(True)))  # 返回值是否正确
        self.assertEqual(is_palindrome_number(1547451), True)
        self.assertEqual(is_palindrome_number(21431), False)


if __name__ == '__main__':
    unittest.main()