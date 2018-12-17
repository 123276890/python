# -*- coding: utf-8 -*-
"""
写一个函数，它接受一个字符串，做的事情和strip()字符串方法一样。如果只
传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。否
则，函数第二个参数指定的字符将从该字符串中去除。
"""


import re


def stripRe(n, m=''):
    if type(n) == str:
        if m == '':
            nRe = re.compile(r'(\s*)(\S*)(\s*)').search(n)
            nRe = nRe.group(2)
            print(nRe)
        else:
            nRe = re.compile((r'[%s]' % m)).findall(n)
            n = n.replace(nRe[0], '')
            print(n)
    else:
        print('TypeError')


n = '  23dfdsfds2fsd""f  '

stripRe(n, '"')