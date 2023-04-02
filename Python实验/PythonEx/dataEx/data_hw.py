#!/usr/bin/python
# -*- coding:UTF-8 -*-
import struct


# 题目十七：二进制数据报文构建与解析
def pack_message(data_dict):
    # 定义数据格式 BB16s>i>iB
    fmt = "2B16s2iB"
    # 将dis1和dis2转换为网络字节
    import socket
    data_dict['dis1'] = socket.htonl(data_dict['dis1'])
    data_dict['dis2'] = socket.htonl(data_dict['dis2'])
    pack = struct.pack(fmt, data_dict['type'], data_dict['csum'], data_dict['id'].encode('utf-8'),
                       data_dict['dis1'], data_dict['dis2'], data_dict['count'])
    unpack = struct.unpack(fmt, pack)
    print(unpack)
    return pack



def unpack_message(message):
    # 定义数据格式 BB16s>i>iB
    fmt = "2B16s2iB"
    unpack = struct.unpack(fmt, message)
    data_dict = {'type': unpack[0], 'csum': unpack[1], 'ID': unpack[2].decode('utf-8'), 'dis1': unpack[3],
                 'dis2': unpack[4], 'count': unpack[5]}
    return data_dict


if __name__ == "__main__":
    data_dict = {'type': 50, 'csum': 1, 'id': 'abcdefghigklmnop', 'dis1': 300, 'dis2': 100, 'count': 20}
    data = pack_message(data_dict)