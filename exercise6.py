# -*- coding: utf-8 -*-
#使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if L == []:
        return (None,None)
    else:
        max = min = L[0]
        for num in L:
            if num < min:
                min = num
            else:
                min = min
        for num in L:
            if max > num:
                max = max
            else:
                max = num

        return min,max




L = []
while True:
    x = input('请输入数字：')
    if x == 'end':
        break
    else:
        x = int(x)
        L.append(x)
print(findMinAndMax(L))