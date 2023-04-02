# -*- coding: UTF-8 -*-

import base64

#题目十五：Base64编解码
def b64en(path_in, path_out):
    import base64
    with open(path_in, 'rb') as f:
        data = f.read()
    with open(path_out, 'w', encoding='utf-8') as f:
        f.write(base64.b64encode(data).decode('utf-8'))


def b64de(path_in, path_out):
    with open(path_in, 'r', encoding='utf-8') as f:
        data = f.read()
    with open(path_out, 'wb') as f:
        # base64解码表
        table = {
            'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
            'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
            'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 'i': 34,
            'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45,
            'u': 46, 'v': 47, 'w': 48, 'x': 49, 'y': 50, 'z': 51, '0': 52, '1': 53, '2': 54, '3': 55, '4': 56,
            '5': 57, '6': 58, '7': 59, '8': 60, '9': 61, '+': 62, '/': 63
        }
        # 解码
        # data = data.replace('\r', '').replace('\n', '')
        # 判断结尾有多少个=
        end = 0
        for i in range(1, 5):
            if data[-i] == '=':
                end += 1
        data = data[:-end]
        # 解码
        result = ''
        for i in range(0, len(data)):
            # 将data[i]的值转换为6位二进制表示，并使用zfill()函数在前面填充零
            result += bin(table[data[i]])[2:].zfill(6)
        # 去除2*end个零
        result = result[:-2 * end]
        # 输出二进制，八位一组，转换为字节
        for i in range(0, len(result), 8):
            f.write(bytes([int(result[i:i+8], 2)]))



if __name__ == '__main__':
    b64en("./pic.jpg", "./pic_en.txt")
    b64de("./pic_en.txt", "./pic_de.jpg")
