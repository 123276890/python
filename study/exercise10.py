# -*- coding: utf-8 -*-
# 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution


class Screen(object):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def resolution(self):
        return self.__width * self.__height


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)