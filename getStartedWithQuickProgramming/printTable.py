# -*- coding: utf-8 -*-
"""
编写一个名为printTable()的函数，它接受字符串的列表的列表，将它显示在组
织良好的表格中，每列右对齐。假定所有内层列表都包含同样数目的字符串。例如，
该值可能看起来像这样
"""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(t):
    w = 0
    for v in t:
        for s in v:
            width = len(s)
            if width > w:
                w = width
            else:
                w = w
    i = 0
    j = 0
    while i < 3:
        while j < 4:
            print(t[i][j].rjust(w), end='')
            i += 1
            if i == 3:
                print('\n')
                i = 0
                j += 1
printTable(tableData)