# -*- coding: utf-8 -*-
#列表数据类型，有序的集合，可以随时添加和删除其中的元素[]
classmate = ['A','B','C']
print(classmate)
print(len(classmate))#获取list元素个数
print(classmate[0])
print(classmate[-1])
classmate.append('D')#末尾添加元素
print(classmate)
classmate.insert(1,'AB')#把元素插入到指定位置
print(classmate)
classmate.pop()
print(classmate)
classmate.pop(1)#删除指定位置元素
print(classmate)
L = [
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Lisa']
]
#打印Apple
print(L[0][0])
#打印python
print(L[1][1])
#打印Lisa
print(L[2][2])


url = 'https://www.autohome.com.cn/grade/carhtml/'


letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
for letter in letters:
    letter = url+letter+'.html'
    print(letter+'123')