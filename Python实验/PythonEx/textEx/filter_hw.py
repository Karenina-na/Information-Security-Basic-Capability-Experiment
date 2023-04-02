# -*- coding: UTF-8 -*-

import os

# 题目十三：C程序文件处理
def filter_c_file(dir_path):
    # 读入所有.c或者.cpp文件
    for item in os.listdir(dir_path):
        if item.endswith(".c") or item.endswith(".cpp"):
            if item.endswith(".c"):
                name = item[:-2]
            else:
                name = item[:-4]
            path = os.path.join(dir_path, item)
            # GPK格式，需要用utf-8编码
            with open(path, 'r', encoding="utf-8") as f:
                lines = f.readlines()
                result = ""
                for line in lines:
                    if line.startswith("#include"):
                        continue
                    elif line.startswith("//"):
                        continue
                    elif line != "\n":
                        if "/*" in line:
                            line = line[:line.index("/*")] + line[line.index("*/") + 2:]
                        if "//" in line:
                            line = line[:line.index("//")]
                        result += line.replace(" ", "").replace("\n", "")
            with open(os.path.join(dir_path, name) + ".txt", 'w', encoding='utf-8') as f:
                f.write(result)


if __name__ == '__main__':
    dir_path = "../testCase/testData"
    filter_c_file(dir_path)
