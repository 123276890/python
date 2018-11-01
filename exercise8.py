# -*- coding: utf-8 -*-
#吧Student对象的gender字段对外隐藏，用get_gender()和set_gender()代替，检查参数有效性


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male':
            self.__gender = gender
        elif gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('bad value')

bart = Student('Bart', 'male')
bart.set_gender('female')
print(bart.get_gender())

