# -*- coding: utf-8 -*-

"""
创建程序multiplicationTable.py，从命令行接受数字N，在一个Excel 电子表格
中创建一个N×N 的乘法表
"""

import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb['Sheet']
print('input Num:')
num = input()
for i in range(1, int(num)+1):
    sheet['A' + str(i+1)] = i
    sheet['A' + str(i+1)].font = Font(bold=True)
    sheet[chr(i+65) + '1'] = i
    sheet[chr(i+65) + '1'].font = Font(bold=True)
    j = i
    while i >= 1:
        sheet[chr(i+65) + str(i+1)] = '=A' + str(i+1) + '*' + chr(i+65) + '1'
        j -= 1
        if j == 0:
            break
        else:
            sheet[chr(i+65) + str(j+1)] = '=A' + str(j+1) + '*' + chr(i+65) + '1'
            sheet[chr(j+65) + str(i+1)] = '=A' + str(i+1) + '*' + chr(j+65) + '1'
    pass


wb.save('multiplicationTable.xlsx')