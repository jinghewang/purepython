# file:fortest.py
# coding:utf-8

__author__ = 'robin'

from time import sleep


def fortest():
    for i in range(1,5):
        if i==3:
            print "continue"
            continue;
        else:
            print "current num:",i
    else:
        print 'for loop is over'


def fortest2():
    for food in "apple", "eggs", "tomatoes":
        print 'i love ', food
