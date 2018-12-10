# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('https://www.cnblogs.com/feng0815/p/8735491.html')
data = driver.page_source
print(data)
tableData = driver.find_element_by_tag_name('tableData').get_attribute('innerHTML')
tableI = driver.find_element_by_tag_name('tableData').get_attribute('id')
tableI = driver.find_element_by_tag_name('tableData').text
driver.quit()