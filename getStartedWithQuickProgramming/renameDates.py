# -*- coding: utf-8 -*-
"""
假定你的老板用电子邮件发给你上千个文件，文件名包含美国风格的日期
（MM-DD-YYYY），需要将它们改名为欧洲风格的日期（DD-MM-YYYY）。手工完
成这个无聊的任务可能需要几天时间！让我们写一个程序来完成它。
"""
# 以美国MM-DD-YYYY日期格式重命名文件名

import shutil, os, re

# 创建一个与美国日期格式的文件匹配的正则表达式。

datePattern = re.compile(r"""^(.*?)                  # all text before the date
    ((0|1)?\d)-                                      # one or two digits for the month
    ((0|1|2|3)?\d)-                                  # one or two digits for the day
    ((19|20)\d\d)                                    # four digits for the year
    (.*?)$                                           # all text after the date
    """, re.VERBOSE)

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    if mo == None:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # 获取完整的、绝对的文件路径。
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    # shutil.move(amerFilename, euroFilename) # uncomment after testing