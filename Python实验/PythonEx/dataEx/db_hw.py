#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目十八：实现数据库的操作
import sqlite3
import os

db_hw_db_path = ""  # 全局变量，在create_db(path)时记录创建的数据库所在路径


def create_db(path):
    pass


# 使用Insert语句
def new_employee(person,level):
    pass


# 使用Delete语句
def delete_employee(person):
    pass


# 使用Update语句
def set_level_salary(level,salary):
    pass


# 使用Select查询语句
def get_total_salary():
    pass


if __name__ == "__main__":
    create_db('./test.db')
    new_employee(("tom","m","2018-09-01","123456789"),"A")
    new_employee(("too","f","2017-09-01","123456788"),"B")
    print(get_total_salary())
    delete_employee("123456788")
    print(get_total_salary())
    set_level_salary("A",2)
    print(get_total_salary())
