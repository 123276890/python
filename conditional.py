# -*- coding: utf-8 -*-
#条件判断
age = int(input('情输入你的年龄:'))#int()强制转换为整数
print(type(age))
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')