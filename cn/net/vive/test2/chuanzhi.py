# file:
# coding:utf-8

__author__ = 'robin'


def test():
    # print f(1)
    # print f(2)
    # print f(3)

    # print f2(1)
    # print f2(2)
    # print f2(3)
    pass


def f(a, L=[]):
    L.append(a)
    return L


def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

