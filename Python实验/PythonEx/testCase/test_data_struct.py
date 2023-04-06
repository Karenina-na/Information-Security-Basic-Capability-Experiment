#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

sys.path.append("../")

import unittest
from dataEx.data_hw import *


# 单元测试
class TestStructFunc(unittest.TestCase):

    # 题目：二进制数据报文构建与解析
    def test_struct_1(self):
        data_dict = {'type': 50, 'csum': 1, 'id': 'abcdefghigklmnop', 'dis1': 300, 'dis2': 100, 'count': 20}
        data = pack_message(data_dict)
        self.assertEqual(data, b'2\x01abcdefghigklmnop\x00\x00\x01,\x00\x00\x00d\x14')

        new_dict = unpack_message(data)
        self.assertDictEqual(new_dict, data_dict)


if __name__ == '__main__':
    unittest.main()
