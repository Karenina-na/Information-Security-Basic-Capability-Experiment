#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../")

import unittest
from numEx.num_hw import *


class TestNarFunc(unittest.TestCase):
    def test_Nar_1(self):
        self.assertTrue(isinstance(narcissistic_number(), type([])))

    def test_Nar_2(self):
        self.assertEqual(narcissistic_number(), [153, 370, 371, 407])

if __name__ == '__main__':
    unittest.main()
