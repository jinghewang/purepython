# file:listtest.py
# coding:utf-8

__author__ = 'robin'


shoplist = ["apple", "bear", "banana"]


def test():
    # map
    ls = range(1, 9);
    ls2 = map(lambda x: x * 2, ls)
    helper.print2(ls2, True)

    # sort
    # ls.sort(lambda x,y:cmp(x,y),key=lambda x:x%5)
    ls2 = sorted(ls, lambda x, y: cmp(x, y), key=lambda x: x % 5)
    helper.print2(ls2,True)

    # filter
    ls2 = filter(lambda x:x>4,ls)
    helper.print2(ls2,True)


def getlen():
    return len(shoplist)


def delfirst():
    del shoplist[0]


def sort(cmp=None, key=None, reverse=False):
    return shoplist.sort(cmp, key, reverse)


def count(x):
    return shoplist.count(x)


def clear():
    global shoplist
    shoplist = []


def append(*items):
    for item in items:
        shoplist.append(item)


def extend(t):
    return shoplist.extend(t)


def insert(i, x):
    shoplist.insert(i, x)


def remove(x):
    return shoplist.remove(x)


def pop(i=-1):
    return shoplist.pop(i)


def index(x):
    return shoplist.index(x)


def reverse():
    return shoplist.reverse()

import cn.net.vive.base.helper as helper


def listout(dividing=False):
    if dividing == True:
        helper.dividing()

    for i in shoplist:
        print(i)
