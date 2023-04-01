#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../")

import unittest
from numEx.num_hw import *


# 单元测试
class TestDistanceFunc(unittest.TestCase):

    # 题目：两地之间距离计算
    def test_sphere_distance_1(self):
        dis = sphere_distance((134.37069, 107.231507), (34.251739, 108.959))
        self.assertEqual(dis, 'Parameter Error.')

    def test_sphere_distance_2(self):
        dis = sphere_distance((34.24, 108.95), (30.89, 121.33))
        self.assertAlmostEqual(dis, 1217.53, delta=100)


if __name__ == '__main__':
    unittest.main()