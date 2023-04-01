"""
利用 Python 实现将 C 源代码文件(后缀 c，.cpp) 读入，去除代码中的空格、块注释、行注释、include 语句、空行、回车换行符号，形成一个长字符串，并写入到新的文件
实现函数:
(1)C/C++文件过滤函数
函数原型: def tilter c file(path)
从 path 中找到后缀为 .c，.pp 的文件，逐个按要求删除不必要的字符，形成一个新字符串，该字符串被写入到同级目录下的新文件“XXXtxt”，其中“XXX”为原C/C++文件文件名称。
参数 path: 需要过滤的 C/C++文件路径，包含有多个文件
返回值:无。
"""


def filter_c_file(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        result = ""
        flag = False
        for line in lines:
            if line.startswith("#include"):
                continue
            elif line.startswith("//"):
                continue
            elif line.startswith("/*"):
                flag = True
                continue
            elif line.startswith("*/"):
                flag = False
                continue
            elif flag:
                continue
            elif line != "\n":
                result += line.replace(" ", "").replace("\n", "")
    with open(path[:-1] + "txt", 'w') as f:
        f.write(result)
