"""
理解 Base64编码的原理，设计两个函数实现二进制数据的编解码。
0
Base64 编码:
函数原型: defb64en(path in,path out)
参数path in:需要进行 base64 编码的图片文件路径参数path out:以UTF8编码生成的文本文件路径返回值:无。可使用 base64 内置库
Base64 解码;(2
函数原型: defb64de(path in,path out)
参数path in:需要进行 base64解码的UTF8文本文件路径参数 path out:解码生成的图片文件路径
返回值:无。不允许使用 base64 内置库
"""


def b64en(path_in, path_out):
    import base64
    with open(path_in, 'rb') as f:
        data = f.read()
    with open(path_out, 'w') as f:
        f.write(base64.b64encode(data).decode('utf-8'))


def b64de(path_in, path_out):
    with open(path_in, 'rb') as f:
        data = f.read()
    with open(path_out, "rb") as f:
        result = []
