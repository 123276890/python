# -*- coding: utf-8 -*-
#定义函数
#定义一个quadratic(a,b,c)，接受三个参数，返回一元二次方程:ax**2+bx+c = 0的两个解
#提示：计算平方根可以调用math.sqrt()
import math
def quadratic(a,b,c):
    b1 = b*b - 4*a*c
    if a == 0:
        return 'a不可为零，请重新输入'
    elif b1 < 0:
        return '原方程无解'
    elif b1 == 0:
        x1 = x2 = -b/2*a
        return x1 , x2
    else:
        x1 = ((-b) + math.sqrt(b1))/(2*a)
        x2 = ((-b) - math.sqrt(b1))/(2*a)
        return x1 , x2
a = int(input('请输入a的值:'))
b = int(input('请输入b的值:'))
c = int(input('请输入c的值:'))
print('x的值为:', quadratic(a,b,c))
