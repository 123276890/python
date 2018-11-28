# -*- coding: utf-8 -*-
# selenium phantomjs


names = ['比T5','2017款','1.5T','自动豪华型']
series = ['比速T5']
if names[:len(series)] == series[:len(series)]:
    pass
else:
    item = " ".join(series[:len(series)+1]) + " " + " ".join(names[len(series):])
print(item)

i = range(1,8)
for x in i:
    print(x)

item = '26262-n'
if item.count('-') > 0:
    item = (item.split("-"))[0]

print(item)