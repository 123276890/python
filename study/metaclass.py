# -*- coding: utf-8 -*-
# 元类


def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


H = type('Hello', (object,), dict(hello=fn))    # 创建Hello class


h = H()
print(H.__name__)

h.hello()