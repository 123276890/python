# -*- coding: utf-8 -*-
#汉诺塔
#编写move(n,a,b,c)函数，接收参数n，表示3个柱子A,B,C中第一个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
def move(n,a,b,c):
    if n == 1:
        print(a,'--->',c)
    else:
        move(n - 1,a,c,b)
        print(a,'--->',c)
        move(n - 1,b,a,c)

move(3,'A','B','C')