# -*- coding: utf-8 -*-

"""
假定你有一张电子表格的数据，来自于2010 年美国人口普查。你有一个无聊的任
务，要遍历表中的几千行，计算总的人口，以及每个县的普查区的数目（普查区就是一
个地理区域，是为人口普查而定义的）。每行表示一个人口普查区。
"""

import openpyxl, pprint, os
print('Opening workbook...')

os.chdir('/Users/zhuangganglong/Downloads/automate_online-materials')
print(os.getcwd())
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # 确保此状态的键存在。
    countyData.setdefault(state, {})

    # 确保这个州的这个县的密钥存在。
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # 每一行代表一个普查区域，因此增加1。
    countyData[state][county]['tracts'] += 1

    # 在这一人口普查范围内增加县人口
    countyData[state][county]['pop'] += int(pop)

print('Writing results...')
os.chdir('/Users/zhuangganglong/python/getStartedWithQuickProgramming')
resultFile = open('censu2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done')
pass