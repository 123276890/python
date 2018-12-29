# -*- coding: utf-8 -*-

"""
编写一个程序，通过命令行接受电子邮件地址和文本字符串。然后利用selenium
登录到你的邮件账号，将该字符串作为邮件，发送到提供的地址（你也许希望为这
个程序建立一个独立的邮件账号）。
"""
import selenium
from selenium import webdriver
import time


# print('input Received email address')
# emailAdress = input()
# print('emailAdress: %s' % emailAdress)
#
# print('input Text string')
#
# textString = input()
# print('Text string: %s' % textString)

browser = webdriver.Chrome()
browser.get('https://mail.163.com/')

now = int(round(time.time() * 1000))
browser.switch_to.frame(browser.find_element_by_tag_name('iframe'))
emailElem = browser.find_element_by_name('email')
emailElem.send_keys('13914564003')
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys('zgl.960504')
btn = browser.find_element_by_id('dologin')
btn.click()
writeBtn = browser.find_element_by_css_selector('li#_mail_component_59_59 span.oz0')
writeBtn.click()
pass
