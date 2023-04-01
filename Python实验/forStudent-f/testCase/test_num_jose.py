#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../")

import unittest
from numEx.num_hw import *


class TestJoseFunc(unittest.TestCase):
    def test_Jose_1(self):
        self.assertTrue(isinstance(jose_prob(1,2), type([])))  # 返回值是否正确
        self.assertEqual(jose_prob(7, 28.9), 'Parameter Error.')

    def test_Jose_2(self):
        self.assertTrue(isinstance(jose_prob(1, 2.8), type('')))  # 返回值是否正确

    def test_Jose_3(self):
        self.assertEqual(jose_prob(15, 30),[1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0])


if __name__ == '__main__':
    unittest.main()
