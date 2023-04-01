#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
sys.path.append("../")
import unittest
from textEx.text_hw import *


# 单元测试
class TestMorseFunc(unittest.TestCase):

    # 题目：morse code
    def test_morse_1(self):
        self.assertTrue(isinstance(morse_code(""), type("")))  # 返回值是否正确

    def test_morse_2(self):
        s = morse_code("i am morse 258")
        self.assertEqual(s,". .       . -   - -       - -   - - -   . - .   . . .   .       . . - - -   . . . . .   - - - . .")

    def test_morse_3(self):
        s = morse_code("I love Python")
        self.assertEqual(s,". .       . - . .   - - -   . . . -   .       . - - .   - . - -   -   . . . .   - - -   - .")

    def test_morse_4(self):
        s = morse_code("I")
        self.assertEqual(s, ". .")


if __name__ == '__main__':
    unittest.main()