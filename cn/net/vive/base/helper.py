# file:
# coding:utf-8

__author__ = 'robin'

# import
import os
import json
from time import sleep


def getfile(name):
    return os.getcwd() + "\\" + name


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


def dividing_with_title(title, msg='-', times=10, times2=10):
    """
    输出分隔线

    :rtype : str
    """
    print msg * times + title + msg * times2
