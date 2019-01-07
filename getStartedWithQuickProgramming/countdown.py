# -*- coding: utf-8 -*-

"""
就像很难找到一个简单的秒表应用程序一样，也很难找到一个简单的倒计时程
序。让我们来写一个倒计时程序，在倒计时结束时报警。
"""

import time, subprocess

timeLeft = 10

while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['open', 'alarm.wav'])