# -*- coding: utf-8 -*-
# 把Student的gender属性改造为枚举类型。可以避免使用字符串


from enum import Enum, unique


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        if type(gender) == Gender:
            self.gender = gender
        else:
            raise TypeError('输入有误')


bart = Student('Bart', Gender.Female)
print(bart.gender)

import re

print(re.compile(r"[\u5ea7]+.*").findall('几门几座几箱车'))