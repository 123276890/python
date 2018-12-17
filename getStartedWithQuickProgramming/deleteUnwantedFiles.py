# -*- coding: utf-8 -*-
"""
一些不需要的、巨大的文件或文件夹占据了硬盘的空间，这并不少见。如果你
试图释放计算机上的空间，那么删除不想要的巨大文件效果最好。但首先你必须找
到它们。
"""

import os

for folderName, subfolders, filenames in os.walk('/Users/zhuangganglong'):
    for f in filenames:
        if len(f) > 0:
            fSource = str(folderName) + '/' + str(f)
            if os.path.getsize(fSource) > int(104857600):
                print(fSource)
