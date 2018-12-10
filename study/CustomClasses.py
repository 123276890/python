# -*- coding: utf-8 -*-
# 定制类


class Student(object):

    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.__name

    __repr__ = __str__

    def __call__(self):
        print('My name is %s' % self.__name)

# print(Student('Michael'))    #<__main__.Student object at 0x10b831438>  不加__str__()方法
print(Student('Michael'))  # Student object (name: Michael)

s = Student('Micha')
print(s)
s()


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


for n in Fib():
    print(n)


f = Fib()
print(f[11])
print(f[:10])