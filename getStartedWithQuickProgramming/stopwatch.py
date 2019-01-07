# -*- coding: utf-8 -*-

"""
假设要记录在没有自动化的枯燥任务上花了多少时间。你没有物理秒表，要为
笔记本或智能手机找到一个免费的秒表应用，没有广告，且不会将你的浏览历史发
送给市场营销人员，又出乎意料地困难（在你同意的许可协议中，它说它可以这样做。
你确实阅读了许可协议，不是吗？）。
"""

import time

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.Press Ctrl-C to quit.')
input()                 # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1
try:
    while True:
        if input() == '1':
            break
        else:
            lapTime = round(time.time() - lastTime, 2)
            totalTime = round(time.time() - startTime, 2)
            print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
            lapNum += 1
            lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone.')