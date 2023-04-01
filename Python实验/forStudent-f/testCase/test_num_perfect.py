#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../")

import unittest
from numEx.num_hw import *


class TestPerfectFunc(unittest.TestCase):
    def test_Per_1(self):
        self.assertTrue(isinstance(perfect_number(), type([])))
        self.assertEqual(perfect_number(0), 'Parameter Error.')

    def test_Per_2(self):
        self.assertEqual(perfect_number(1000), [6, 28, 496])


if __name__ == '__main__':
    unittest.main()
