# coding:utf-8
# module:func.py


__author__ = 'robin'
appid = 'hlt'


def foo():  # 一个函数
    print 'foo:', appid


def foo2(msg):
    return appid, ':', msg


def floor(number):
    result = 0
    while result <= number:
        result = result + 1
    result = result - 1
    return result


def sum2(x, y):
    return x + y;


def area(w, h):
    return w*h


class bar:
    def grok(self):
        print 'I am ok'
