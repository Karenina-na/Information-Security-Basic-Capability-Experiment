#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

sys.path.append("../")

import unittest
from textEx.text_hw import *


# 单元测试
class TestWordFunc(unittest.TestCase):

    # 题目：词频统计
    def test_word_1(self):
        li = word_freq('./testData/text0.txt')
        self.assertListEqual(li, [('b', 16), ('shorts', 4), ('ok', 4), ('dollars', 4), ('welcome', 2), ('twenty', 2),
                                  ('thanks', 2), ('purple', 2), ('nice', 2), ('need', 2)])


if __name__ == '__main__':
    unittest.main()
