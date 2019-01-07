# -*- coding: utf-8 -*-

"""
Excel 可以将电子表格保存为CSV 文件
"""

import os, openpyxl, csv

os.chdir('/Users/zhuangganglong/python/getStartedWithQuickProgramming/excelSpreadsheets')
for fileName in os.listdir('.'):                                                     # 循环遍历当前目录文件夹
    if not fileName.endswith('.xlsx'):                                               # 如果不是Excel文档就跳过，继续循环下一步
        continue
    print('Transforming ' + fileName + ' to CSV...')                                 # 输出显示当前正在转换的文件名
    wb = openpyxl.load_workbook(fileName)

    for sheetName in wb.sheetnames:  # 循环遍历当前文档中的工作表
        sheet = wb[sheetName]
        csvFile = open(fileName[:-5] + '_' + sheetName + '.csv', 'w', newline='')  # 创建一个CSV的FILE对象，根据项目要求命名
        csvWriter = csv.writer(csvFile)  # 创建一个writer对象
        for rowNum in range(1, sheet.max_row + 1):  # 循环当前工作表中的每一行
            rowData = []
            for colNum in range(1, sheet.max_column + 1):  # 循环当前行中的每一列，即每个单元格
                rowData.append(sheet.cell(row=rowNum, column=colNum).value)  # 将单元格值插入到列表中，形成包含Excel每行数据的列表
            csvWriter.writerow(rowData)  # 用writerow()方法将列表写入CSV文档

print('Done!')
