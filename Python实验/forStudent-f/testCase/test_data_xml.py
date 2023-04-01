#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../")

import unittest, os
from dataEx.xml_hw import *

try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et


# 单元测试
class TestXmlFunc(unittest.TestCase):
    # 题目：XML文件的生成和解析
    def test_Xml_1(self):
        path = "./created.xml"
        if os.path.exists(path):
            os.remove(path)

        create_xml(path)
        self.assertTrue(os.path.exists(path))

        d = parse_xml(path)
        self.assertDictEqual(d,{'tilemap service': 'http://tms.osgeo.org/1.0.0', 'title': 'default', 'tileset count': 6, 'tileset max': 5})


if __name__ == '__main__':
    unittest.main()