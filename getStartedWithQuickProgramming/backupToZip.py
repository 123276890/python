# -*- coding: utf-8 -*-

"""
假定你正在做一个项目，它的文件保存在C:\AlsPythonBook 文件夹中。你担心工作
会丢失，所以希望为整个文件夹创建一个ZIP 文件，作为“快照”。你希望保存不同的版
本，希望ZIP 文件的文件名每次创建时都有所变化。例如AlsPythonBook_1.zip、
AlsPythonBook_2.zip、AlsPythonBook_3.zip，等等。你可以手工完成，但这有点烦人，
而且可能不小心弄错ZIP 文件的编号。运行一个程序来完成这个烦人的任务会简单得多。
"""

import zipfile, os


def backupToZip(folder):
    # 将“文件夹”的全部内容备份到ZIP文件中。
    folder = os.path.abspath(folder)                # make sure folder is absolute
    # 找出这个代码应该基于的文件名
    # 哪些文件已经存在。
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # 创建ZIP文件。
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # 遍历整个文件夹树并压缩每个文件夹中的文件。
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
    # 将当前文件夹添加到ZIP文件。
        backupZip.write(foldername)
    # 将该文件夹中的所有文件添加到ZIP文件中。
    for filename in filenames:
        newBase = os.path.basename(folder) + '_'
        if filename.startswith(newBase) and filename.endswith('.zip'):
            continue    # 不要备份备份的ZIP文件
        backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')
    backupToZip('C:\\delicious')