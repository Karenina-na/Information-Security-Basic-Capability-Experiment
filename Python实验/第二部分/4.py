"""
提供一个敏感词库文件 sensitive.txt，敏感词按类型进行分组，如“第一类 形容词”，每组中一行代表一个敏感词，如“可泊”。要求读取敏感词库，获得敏感词列表，根据敏感词列表对输入的敏感词进行过滤。敏感词是几个字，就将对应的文本替换成几个*符号。比如敏感词为脉动，则将“脉动真好喝”替换为“**真好喝”。
注意敏感词类型文本不归入敏感词，比如“第一类 形容词”不在过滤范围。敏感词库文件中的行可能只有空格，读入时请去除，不包含在过滤词库中。
函数原型: def filter words(user input)
参数 user input:字符串，为输入待处理的字符串返回值:字符串，过滤后的字符串
"""


def filter_words(user_input):
    with open("sensitive.txt", 'r') as f:
        lines = f.readlines()
        sensitive_words = []
        for line in lines:
            if line != "\n" and not line.startswith("第"):
                sensitive_words.append(line.replace("\n", ""))
    for word in sensitive_words:
        user_input = user_input.replace(word, "*" * len(word))
    return user_input
