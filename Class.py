# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_mes(std):
        print('%s: %s' % (std.name, std.score))

    def get_graid(self):
        if self.score >=90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'


def print_mes(std):
   print('%s: %s' % (std.name, std.score))


mark = Student('Mark', 60)
print_mes(mark)

mark.print_mes()
print(mark.get_graid())