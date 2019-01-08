# -*- coding: utf-8 -*-

"""
假定你一直“自愿”为“强制自愿俱乐部”记录会员会费。这确实是一项枯燥
的工作，包括维护一个电子表格，记录每个月谁交了会费，并用电子邮件提醒那些
没交的会员。不必你自己查看电子表格，而是向会费超期的会员复制和粘贴相同的
电子邮件。
"""

import openpyxl, smtplib, sys
wb = openpyxl.load_workbook('duesRecords.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
lastCol = sheet.get_highest_column()
latestMonth = sheet.cell(row=1, column=lastCol).value

unpaidMembers = {}
for r in range(2, sheet.get_highest_row() + 1):
    payment = sheet.cell(row=r, column=lastCol).value
    if payment != 'paid':
        name = sheet.cell(row=r, column=1).value
        email = sheet.cell(row=r, column=2).value
        unpaidMembers[name] = email