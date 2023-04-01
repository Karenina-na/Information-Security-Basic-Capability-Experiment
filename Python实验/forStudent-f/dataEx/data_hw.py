#!/usr/bin/python
# -*- coding:UTF-8 -*-
import struct


# 题目十七：二进制数据报文构建与解析
def pack_message(data_dict):
    pass


def unpack_message(message):
    pass


if __name__ == "__main__":
    data_dict = {'type': 50, 'csum': 1, 'id': 'abcdefghigklmnop', 'dis1': 300, 'dis2': 100, 'count': 20}
    data = pack_message(data_dict)