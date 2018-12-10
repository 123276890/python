# -*- coding: utf-8 -*-
#杨辉三角
def triangles():
    ret = [1]
    while True:
        yield ret
        ret,retR = ret + [0],[0] +ret
        # print(ret,retR)
        for i in range(1,len(ret)):
            ret[i]= ret[i]+retR[i]

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break