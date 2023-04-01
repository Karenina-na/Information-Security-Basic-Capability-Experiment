#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
sys.path.append("../")

import unittest
from dataEx.db_hw import *


# 单元测试
class TestSqlite3Func(unittest.TestCase):
    # 题目：实现数据库的操作
    def test_db_1(self):
        path = './test.db'
        if os.path.exists(path):
            os.remove(path)

        create_db(path)
        self.assertTrue(os.path.exists(path))
        new_employee(("tom","m","2018-09-01","123456789"),"A")
        new_employee(("too","f","2017-09-01","123456788"),"B")

        self.assertEqual(get_total_salary(),16000)
        delete_employee("123456788")
        set_level_salary("A",2)
        self.assertEqual(get_total_salary(),2)

if __name__ == '__main__':
    unittest.main()