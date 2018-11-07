# -*- coding: utf-8 -*-
# selenium phantomjs


from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('http://www.baidu.com')
print(driver.page_source)