# -*- coding: utf-8 -*-

"""
写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。强口令的
定义是：长度不少于8 个字符，同时包含大写和小写字符，至少有一位数字。你可
能需要用多个正则表达式来测试该字符串，以保证它的强度。
"""
import re


def passwordDetection(n):
    wRe = re.compile(r".{8,}")
    uRe = re.compile(r"[A-Z]+")
    lRe = re.compile(r"[a-z]+")
    dRe = re.compile(r"\d+")

    if wRe.search(n) != None:
        if uRe.search(n) != None:
            if lRe.search(n) != None:
                if dRe.search(n) != None:
                    print('强口令')
                else:
                    print('不符合')
            else:
                print('不符合')
        else:
            print('不符合')
    else:
        print('不符合')

n = 'AAa123456'
passwordDetection(n)