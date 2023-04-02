#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目十八：实现数据库的操作
import sqlite3
import os

db_hw_db_path = ""  # 全局变量，在create_db(path)时记录创建的数据库所在路径


def create_db(path):
    # 创建数据库
    global db_hw_db_path
    db_hw_db_path = path
    if os.path.exists(path):
        os.remove(path)
    conn = sqlite3.connect(path)
    c = conn.cursor()

    try:
        # 职位表，POSITIONID为主键，SALARY为薪水
        c.execute('''
            CREATE TABLE Position (
            POSITIONID CHAR(9) PRIMARY KEY NOT NULL UNIQUE,
            SALARY INT NOT NULL
            );''')

        # 增加职位，职位ID和薪水
        c.execute("INSERT INTO Position VALUES ('A', 10000)")
        c.execute("INSERT INTO Position VALUES ('B', 6000)")
        c.execute("INSERT INTO Position VALUES ('C', 3000)")
        c.execute("INSERT INTO Position VALUES ('D', 1000)")

        # 人员表，ID为主键，POSITIONID为外键
        c.execute('''CREATE TABLE Person (
            NAME CHAR(32),
            GENDER CHAR(2),
            BIRTH DATE,
            ID CHAR(18) PRIMARY KEY NOT NULL UNIQUE,
            POSITIONID CHAR(9) NOT NULL,
            CONSTRAINT POSITIONID FOREIGN KEY(POSITIONID) REFERENCES Position(POSITIONID)
            );''')

        conn.commit()
    except:
        conn.rollback()
        return -1
    finally:
        conn.close()
    return 0


# 使用Insert语句
def new_employee(person, level):
    # person (name, gender, birth, id)
    conn = sqlite3.connect(db_hw_db_path)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO Person VALUES (?,?,?,?,?)", (person[0], person[1], person[2], person[3], level))
        conn.commit()
    except:
        conn.rollback()
        return -1
    finally:
        conn.close()
    return 0


# 使用Delete语句
def delete_employee(person):
    conn = sqlite3.connect(db_hw_db_path)
    c = conn.cursor()
    try:
        c.execute("DELETE FROM Person WHERE ID = ?", (person,))
        conn.commit()
    except:
        conn.rollback()
        return -1
    finally:
        conn.close()
    return 0


# 使用Update语句
def set_level_salary(level, salary):
    conn = sqlite3.connect(db_hw_db_path)
    c = conn.cursor()
    try:
        # 多表更新，使用JOIN连接 Person和Position
        c.execute("UPDATE Position SET SALARY = ? WHERE POSITIONID = ?", (salary, level))
        conn.commit()
    except:
        conn.rollback()
        return -1
    finally:
        conn.close()
    return 0


# 使用Select查询语句
def get_total_salary():
    conn = sqlite3.connect(db_hw_db_path)
    c = conn.cursor()
    try:
        # 多表查询，使用JOIN连接 Person和Position
        c.execute("SELECT SUM(SALARY) FROM Person JOIN Position ON Person.POSITIONID = Position.POSITIONID")
        result = c.fetchone()
        return result[0]
    except:
        conn.rollback()
    finally:
        conn.close()
    return -1


if __name__ == "__main__":
    print(create_db('./test.db'))
    new_employee(("tom", "m", "2018-09-01", "123456789"), "A")
    new_employee(("too", "f", "2017-09-01", "123456788"), "B")
    print(get_total_salary())
    delete_employee("123456789")
    print(get_total_salary())
    set_level_salary("A", 2)
    set_level_salary("B", 2)
    print(get_total_salary())
