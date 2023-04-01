"""
利用 Python 从文本文件中提取出现频次前十的单词，完成函数:
(1) 词频提取函数:
函数原型: defword freq(path)
参数 path:字符串，需要提取的文本文件路径
返回值:列表，列表元素为二元组(单词，次数):按从多到少的顺序列举出现最多的前十个单词与次数。如果单词出现的次数相同，则按单词的降序排序。统计时去除高频词(见sight word.txt)。
可逐行读取文本内容，并按空格进行切分，逐个统计该行单词的数目信息，存储于字典中，最终对字典中的数据进行排序，可转化为列表之后排序，输出前 10 个出现频率最高的单词及其出现的次数。单词不区分大小写，处理时需去除一些非必要的符号(!~@#S%^&*0 -+=18/?.:"<V>)，只保留单词，连写词如 its，dont等算一个词汇
"""


def word_freq(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        words = []
        for line in lines:
            words += line.split()
        words = [word.strip('!~@#S%^&*0 -+=18/?.:"<V>') for word in words]
        words = [word.lower() for word in words]
        freq = {}
        for word in words:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return freq[:10]