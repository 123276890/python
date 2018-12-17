# -*- coding: utf-8 -*-
"""
编写一个程序，遍历一个目录树，查找特定扩展名的文件（诸如.pdf 或.jpg）。
不论这些文件的位置在哪里，将它们拷贝到一个新的文件夹中。
"""

import os, re, shutil

for folderName, subfolders, filenames in os.walk('/Users'):
    nRe = re.compile(r'\s*((.pdf|.jpg|.png)+)')
    for f in filenames:
        if len(f) > 0:
            if nRe.search(f) != None:
                fSource = str(folderName) + '/' + str(f)
                print(fSource)
                shutil.copy(fSource, '/Users/zhuangganglong/pic')
