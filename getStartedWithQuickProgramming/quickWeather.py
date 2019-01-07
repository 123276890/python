# -*- coding: utf-8 -*-

"""
检查天气似乎相当简单：打开Web 浏览器，点击地址栏，输入天气网站的URL
（或搜索一个，然后点击链接），等待页面加载，跳过所有的广告等。
"""


import json, requests, sys

print('your location')
location = input()

# London 524901
url ='https://samples.openweathermap.org/data/2.5/forecast/daily?id=%s&appid=b1b15e88fa797225412429c1c50c122a1' % (location)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
