#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../")

import unittest
import base64
from textEx.base64_hw import *


class TestNumFunc(unittest.TestCase):
    def test_b64_1(self):
        b64en("./testData/pic.jpg", "./testData/pic_en.txt")
        b64de("./testData/pic_en.txt", "./testData/pic_de.jpg")

        with open("./testData/pic.jpg", "rb") as f1:
            temp_11_1 = f1.read()
            f1.close()
        with open("./testData/pic_de.jpg", "rb") as f2:
            temp_11_2 = f2.read()
            f2.close()

        self.assertEqual(temp_11_1, temp_11_2)



if __name__ == '__main__':
    unittest.main()
