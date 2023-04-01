# -*- coding: utf-8 -*-
"""
利用 Pvthon 实现地求上两点之间的距离计算，地球上点的位置以经纬度坐标形式提供。距离计算采用 Haversine 公式:
d = 2r arcsinhav(P2 -P)+cos(P1)cos(P2)hav(A2-)926+cos(P1)cos(P2)sin2=2rarcsinsin
这里r是地球半径 6371Km，(o,)代表点的(纬度，经度) 坐标参考网站: https://en.wikipedia.org/wiki/Haversine formula完成距离计算函数:
函数原型: defsphere distance(p1,p2)
参数 pl: tuple 元组类型，二元组，(练度，经度)，坐标精确到小数点后7位
参数 p2: tuple 元组类型，二元组， (纬度，经度)，坐标精确到小数点后 7位
纬度取值范围:[0-90]，经度取值范围:0-1801，单位均为角度;而 Haversine 公式计算采用的是弧度，注意转换。
返回值:如果输入的坐标数据合规，则返回两点之间的距离，单位为 Km，保留两位小如果输入的坐标不合规，返回错误“Parameter Error.
"""
import math
import numpy as np


def sphere_distance(pos1: (float, float), pos2: (float, float)) -> float or str:
    def hav(theta: float) -> float:  # 弧度的hav值
        return (1 - math.cos(theta)) / 2

    def toRad(theta: float) -> float:  # 角度转弧度
        return theta * math.pi / 180

    R = 6371  # 地球半径
    lat1, lon1 = pos1
    lat2, lon2 = pos2
    if lat1 > 90 or lat1 < 0 or lat2 > 90 or lat2 < 0 or lon1 > 180 or lon1 < 0 or lon2 > 180 or lon2 < 0:
        return "Parameter Error."
    lat1, lon1, lat2, lon2 = map(toRad, [lat1, lon1, lat2, lon2])
    d = 2 * R * math.asin(math.sqrt(hav(lat2 - lat1) + math.cos(lat1) * math.cos(lat2) * hav(lon2 - lon1)))
    return round(d, 2)


if __name__ == "__main__":
    print(sphere_distance((39.92816697, 116.38954991), (39.93816697, 116.39954991)))

