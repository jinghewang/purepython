# file:
# coding:utf-8

__author__ = 'robin'


def print2(obj, isdivi=False):
    if isdivi:
        dividing()
    print obj


def dividing(msg='-', times=20):
    """
    输出分隔线

    :rtype : str
    """
    print(msg * times)
