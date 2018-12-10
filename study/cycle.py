# -*- coding: utf-8 -*-
#循环
#第一种 for ... in ...
names = ['A','B','C']
for name in names:
    print(name)
#计算1-10的整数之和
sum = 0;
for x in[1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
    # print(sum)#输出每次结果
print(sum)#输出最后一次结果
print(range(5))
print(list(range(5)))#转换为list
#1-100的整数之和
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
#第二种 while
#计算100以内奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
#请利用循环依次对list中的每个名字打印出hello,xxx
L = ['Bart','Lisa','Adam']
for l in L:
    print('hello,'+l)
#break
n = 1
while n <= 100:
    if n>10:
        break
    print(n)
    n = n+1
print('END')
#continue
n = 0
while n < 10:
    n = n+1
    if n % 2 ==0:
        continue
    print(n)