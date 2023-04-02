#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from xml.dom import minidom

try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et


# 题目十六：XML文件的生成和解析
def create_xml(path):
    # 创建xml文件
    root = et.Element("tilemap")
    root.set("tilemapservice", "http://tms.osgeo.org/1.0.0")
    root.set("version", "1.0.0")
    # 子节点
    title = et.SubElement(root, "title")
    title.text = "default"
    abstract = et.Element("abstract")
    root.append(abstract)
    srs = et.SubElement(root, "srs")
    srs.text = "EPSG:4326"
    vsrs = et.Element("vsrs")
    root.append(vsrs)
    boundingbox = et.SubElement(root, "boundingbox")
    boundingbox.set("maxx", "180.0")
    boundingbox.set("maxy", "90.0")
    boundingbox.set("minx", "-180.0")
    boundingbox.set("miny", "-90.0")
    origin = et.SubElement(root, "origin")
    origin.set("x", "-180.0")
    origin.set("y", "-90.0")
    tileformat = et.SubElement(root, "tileformat")
    tileformat.set("extension", "tif")
    tileformat.set("height", "17")
    tileformat.set("mime-type", "image/tiff")
    tileformat.set("width", "17")
    tilesets = et.SubElement(root, "tilesets")
    tilesets.set("profile", "global-geodetic")
    # 子节点的子节点
    pixels=['10.588', '5.294', '2.647', '1.323', '0.661', '0.331']
    for i in range(6):
        tileset = et.SubElement(tilesets, "tileset")
        tileset.set("href", "")
        tileset.set("order", str(i))
        tileset.set("units-per-pixel", pixels[i])
    # 写入文件
    tree = et.ElementTree(root)
    tree.write(path, encoding="utf-8", xml_declaration=True)


def parse_xml(path):
    d = {}
    # 解析xml文件
    tree = et.parse(path)
    root = tree.getroot()
    d["tilemap service"] = root.get("tilemapservice")
    d["title"] = root.find("title").text
    d["tileset count"] = len(root.findall("tilesets/tileset"))
    d["tileset max"] = int(root.find("tilesets/tileset[@order='5']").get("order"))
    return d


if __name__ == "__main__":
    create_xml("./created.xml")
    print(parse_xml("./created.xml"))
