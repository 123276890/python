# -*- coding: utf-8 -*-
# selenium phantomjs


names = ['比T5','2017款','1.5T','自动豪华型']
series = ['比速T5']
if names[:len(series)] == series[:len(series)]:
    pass
else:
    item = " ".join(series[:len(series)+1]) + " " + " ".join(names[len(series):])
print(item)