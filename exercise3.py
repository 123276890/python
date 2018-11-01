# -*- coding: utf-8 -*-
#函数计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积
def product(*num):
    if len(num) != 0:
        sum = 1
        for n in num:
            sum *= n
        return sum
    else:
        raise TypeError

num = []
while True:
    x = int(input('请输入数字'))
    if x == 0:
        break
    num.append(x)
print(num)

print(product(*num))