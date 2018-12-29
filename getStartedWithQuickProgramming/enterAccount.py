# -*- coding: utf-8 -*-

"""
编写一个程序，通过命令行接受电子邮件地址和文本字符串。然后利用selenium
登录到你的邮件账号，将该字符串作为邮件，发送到提供的地址（你也许希望为这
个程序建立一个独立的邮件账号）。
"""
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


print('input Received email address')
emailAdress = input()
print('emailAdress: %s' % emailAdress)

print('input Text string')
textString = input()
print('Text string: %s' % textString)

print('input Password')
password = input()
print('password string: %s' % password)

browser = webdriver.Firefox(executable_path='/Users/zhuangganglong/Desktop/geckodriver')
browser.get('https://mail.163.com/')

time.sleep(3)
now = int(round(time.time() * 1000))
browser.switch_to.frame(browser.find_element_by_tag_name('iframe'))
emailElem = browser.find_element_by_name('email')
emailElem.send_keys('13914564003')
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys(password)
btn = browser.find_element_by_id('dologin')
btn.click()
browser.switch_to.default_content()
writeBtn = browser.find_element_by_css_selector('li#_mail_component_59_59 span.oz0')
writeBtn.click()
recipient = browser.find_element_by_xpath('//label[starts-with(@id,"_mail_emailtips_0")]')
recipient.click()
recipientW = browser.find_element_by_css_selector('div.js-component-emailinput input')
recipientW.send_keys(emailAdress)
browser.switch_to.frame(browser.find_element_by_class_name('APP-editor-iframe'))
body = browser.find_element_by_tag_name('body')
body.send_keys(textString)
browser.switch_to.default_content()
browser.find_element_by_xpath('//footer/div[1]').click()
ActionChains(browser).send_keys(Keys.ENTER).perform()
pass
