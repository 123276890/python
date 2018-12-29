# -*- coding: utf-8 -*-
"""
2048 是一个简单的游戏，通过箭头向上、下、左、右移动滑块，让滑块合并。
实际上，你可以通过一遍一遍的重复“上、右、下、左”模式，获得相当高的分数。
编写一个程序，打开https://gabrielecirulli.github.io/2048/上的游戏，不断发送上、右、
下、左按键，自动玩游戏。
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

broswer = webdriver.Firefox(executable_path='/Users/zhuangganglong/Desktop/geckodriver')
broswer.get('https://play2048.co/')
while True:
    for i in str(random.randint(0, 3)):
        if i == '0':
            ActionChains(broswer).send_keys(Keys.UP).perform()
        elif i == '1':
            ActionChains(broswer).send_keys(Keys.DOWN).perform()
        elif i == '2':
            ActionChains(broswer).send_keys(Keys.RIGHT).perform()
        else:
            ActionChains(broswer).send_keys(Keys.LEFT).perform()

        time.sleep(1)

        try:
            broswer.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div/a[2]').click()
        except:
            pass


