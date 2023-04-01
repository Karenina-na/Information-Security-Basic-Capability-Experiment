# -*- coding: utf-8 -*-
"""
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几
何?
函数原型: defbuy chicken(
返回值:返回一个 list，数列的元素为三元组，代表(鸡翁、鸡母、鸡雏)的数量，如:[T0,25,751,[4,18,781,[8,11,811，表示返回三组解，每一组解以三元 list 表示
"""


def Chi() -> []:
    result = []
    for i in range(0, 21):
        for j in range(0, 34):
            k = 100 - i - j
            if 5 * i + 3 * j + k / 3 == 100:
                result.append([i, j, k])
    return result


if __name__ == "__main__":
    print(Chi())
