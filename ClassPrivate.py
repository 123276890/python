# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

mark = Student('Mark',95)
kid = Student('kid', 50)
# kid.set_score(-1)

print(mark.get_score())
print(kid.get_score())

print(mark._Student__name)

mark.print_score()
# print(mark.__score)  #无法外部调取