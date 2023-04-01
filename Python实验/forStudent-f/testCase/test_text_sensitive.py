#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../")

import unittest
from textEx.text_hw import *


class TestSensiFunc(unittest.TestCase):
    def test_sensi_1(self):
        self.assertTrue(isinstance(filter_words(''), type('')))  # 返回值是否正确

    def test_sensi_2(self):
        self.assertEqual(filter_words("哇哈哈真变态！"), "***真**！")


if __name__ == '__main__':
    unittest.main()
