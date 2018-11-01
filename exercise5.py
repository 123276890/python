# -*- coding: utf-8 -*-
#利用切片，实现trim()函数，去除字符串首尾空格
#切片 slice操作符 :
def trim(s):
    if s[:1] == ' ' and s[-1:] == ' ':
        return s[1:-1]
    elif s[:1] == ' ':
        return s[1:]
    elif s[-1:] == ' ':
        return s[:-1]
    else:
        return s
s = input("请输入文字：")       #条件判断顺序执行
print(trim(s))

def trim2(a):
    if len(a) > 0:
        for item in a:
            if a[0] == ' ':
                a = a[1:]
            else:
                break
        for item in a:
            if a[-1] == ' ':
                a = a[:-1]
            else:
                break
        return a
    else:
        return ''
a = input("请输入文字：")      #for循环 return既跳出循环
print(trim2(a))

