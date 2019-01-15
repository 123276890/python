# -*- coding: utf-8 -*-

"""
能够确定鼠标的位置，对于建立GUI 自动化脚本是很重要的。但光看屏幕，几
乎不能弄清楚像素的准确坐标。如果有一个程序在移动鼠标时随时显示 x y 坐标，
就会很方便。
"""

import pyautogui
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'x: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        IM = pyautogui.screenshot()
        pixelColor = IM.getpixel((x, y))
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')
