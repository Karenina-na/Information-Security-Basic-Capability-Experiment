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
    pass


def parse_xml(path):
    pass


if __name__ == "__main__":
    create_xml("./created.xml")
    print(parse_xml("./created.xml"))