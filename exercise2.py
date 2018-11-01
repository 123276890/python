# -*- coding: utf-8 -*-
#小明身高1.75，体重80.5kg。请根据BMI公式(体重除以身高的平方)帮小明计算他的BMI指数，并根据BMI指数
h = float(input('请输入你的身高：'))
w = float(input('请输入你的体重：'))
bmi = w/(h*h)
print(bmi)
q = ''
if bmi <18.5:
    q = '过轻'
elif bmi <=25:
    q = '正常'
elif bmi <= 28:
    q = '过重'
elif bmi <=32:
    q = '肥胖'
else:
    q = '严重肥胖'
print(q)