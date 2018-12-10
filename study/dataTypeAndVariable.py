# -*- coding: utf-8 -*-
#数据类型和变量
#转义字符\
print('I\'m ok.')
print('I\'m learning\nPython')
print('\\\n\\')
print('\\\t\\')
print(r'\\\t\\')#r''...''表示字符串默认不转义
print('''line1
line2
line3
...''')#'''...'''表示多行内容
print(r'''hello,\n
world''')#转义字符无效
print(True and True)#布尔值
print('hello,%s'%'world')
print('%2d-%02d'%(3,1))#是否补0
print('%.2f'%3.1415926)#小数位数
print('hello,{0},成绩提升{1:.1f}%'.format('小米',17.125))
