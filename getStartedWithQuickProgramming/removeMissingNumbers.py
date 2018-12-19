# -*- coding: utf-8 -*-
"""
编写一个程序，在一个文件夹中，找到所有带指定前缀的文件，诸如spam001.txt,
spam002.txt 等，并定位缺失的编号（例如存在spam001.txt 和spam003.txt，但不存
在spam002.txt）。让该程序对所有后面的文件改名，消除缺失的编号。
"""

import os, re, shutil

fName = re.compile(r'spam(\d{3})\.txt')
NFname = []

for foldername, subfoldersm, filename in os.walk('/Users/zhuangganglong/explore'):
    for f in filename:
        if fName.search(f) != None:
            fSource = str(foldername) + '/' + str(f)
            NFname.append(fSource)
            NFname.sort()
print(NFname)


def checkNF(num):
    if len(str(num + 1)) == 1:
        check = NFname[num][:-7] + "00" + str(num + 1) + NFname[num][-4:]
    elif len(str(num + 1)) == 2:
        check = NFname[num][:-7] + "0" + str(num + 1) + NFname[num][-4:]
    else:
        check = NFname[num][:-7] + str(num + 1) + NFname[num][-4:]
    return check


for h in range(len(NFname)):
    CFname = checkNF(h)
    if NFname[h] != CFname:
        shutil.move(NFname[h], CFname)