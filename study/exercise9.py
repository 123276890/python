# -*- coding: utf-8 -*-
#统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        # self.__class__.count += 1
        Student.count += 1

print(Student.count)
bart = Student('Bart')
print(Student.count)
art = Student('art')
print(Student.count)
