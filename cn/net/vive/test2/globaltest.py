# file:globaltest.py
# coding:utf-8

__author__ = 'robin'


# var
x = 50
y = 100


def maintest():
    globaltest(x)
    print 'x still is',x


def maintest2():
    globaltest2(x)
    print 'y still is', y


def globaltest(x):
    print 'x1', x
    x = 2;
    print "x2", x


def globaltest2(x):
    global y
    print 'y1',y
    y = x
    print 'y2',y
