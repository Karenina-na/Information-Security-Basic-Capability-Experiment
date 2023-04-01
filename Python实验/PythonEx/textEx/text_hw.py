#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 题目十一：摩斯码生成器
def morse_code(usr_str):
    dict = {
        'A': '. -',
        'B': '- . . .',
        'C': '- . - .',
        'D': '- . .',
        'E': '.',
        'F': '. . - .',
        'G': '- - .',
        'H': '. . . .',
        'I': '. .',
        'J': '. - - -',
        'K': '- . -',
        'L': '. - . .',
        'M': '- -',
        'N': '- .',
        'O': '- - -',
        'P': '. - - .',
        'Q': '- - . -',
        'R': '. - .',
        'S': '. . .',
        'T': '-',
        'U': '. . -',
        'V': '. . . -',
        'W': '. - -',
        'X': '- . . -',
        'Y': '- . - -',
        'Z': '- - . .',
        '0': '- - - - -',
        '1': '. - - - -',
        '2': '. . - - -',
        '3': '. . . - -',
        '4': '. . . . -',
        '5': '. . . . .',
        '6': '- . . . .',
        '7': '- - . . .',
        '8': '- - - . .',
        '9': '- - - - .',
    }
    usr_str = usr_str.upper()
    result = ''
    for i in usr_str:
        if i == ' ':
            result += '    '
        else:
            result += dict[i] + '   '
    return result.strip()


# 题目十二：词频统计
def word_freq(path):
    import re
    with open("./testData/sight word.txt", 'r') as f:
        sight_words = f.readline().split()
    with open(path, 'r') as f:
        lines = f.readlines()
        words = []
        for line in lines:
            line = re.sub(r'[!~@#S%^&*0_\-+=8/?,.:"<V>]+', ' ', line)
            words += line.split(' ')
        words = [word.lower() for word in words]
        freq = {}
        for word in words:
            word = word.strip()
            if word in sight_words:
                continue
            if word not in freq and word != '' and word != '\n':
                freq[word] = 1
            elif word != '' and word != '\n':
                freq[word] += 1
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return freq[:10]


# 题目十四：敏感词过滤
def filter_words(user_input):
    pass


if __name__ == '__main__':
    li = morse_code('I love Python')
    print(li)
