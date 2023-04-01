# -*- coding: utf-8 -*-
"""
有15个基督徒和15 个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15 个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从 1 报数报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉 15 个人。由于上帝的保佑，15 个基督徒都幸免于难，问这些人最开始是怎么站的
"""


def main(n: int, m: int) -> [] or str:
    if not isinstance(n, int) or not isinstance(m, int):
        return "Parameter Error"
    Total = [True] * m
    count = 1
    while Total.count(True) > n:
        for i in range(m):
            if Total[i]:
                if count == 9:
                    Total[i] = False
                    count = 1
                else:
                    count += 1
    # 计算初始位置，1代表基督徒，0代表非基督徒
    result = []
    for i in range(m):
        if Total[i]:
            result.append(1)
        else:
            result.append(0)
    return result


if __name__ == "__main__":
    print(main(1, 2))
