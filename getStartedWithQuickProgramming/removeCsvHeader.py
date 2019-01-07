# -*- coding: utf-8 -*-


"""
假设你有一个枯燥的任务，要删除几百CSV 文件的第一行。也许你会将它们送入一
个自动化的过程，只需要数据，不需要每列顶部的表头。可以在Excel 中打开每个文件，
删除第一行，并重新保存该文件
"""

import csv, os

os.makedirs('headerRemoved', exist_ok=True)
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    print('Removing header from ' + csvFilename + '...')

    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue                # skip first row
        csvRows.append(row)
    csvFileObj.close()

    for csvFilename in os.listdir('.'):
        if not csvFilename.endswith('.csv'):
            continue
        csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w',
                          newline='')
        csvWriter = csv.writer(csvFileObj)
        for row in csvRows:
                csvWriter.writerow(row)
        csvFileObj.close()