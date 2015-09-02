# file:using_list.py
# coding:utf-8

__author__ = 'robin'


shoplist = ["apple", "bear", "banana"]


def getlen():
    return len(shoplist)


def getfirst():
    return shoplist[0]


def delfirst():
    del shoplist[0]


def sort():
    shoplist.sort()


def append(item):
    shoplist.append(item)


def insert(i, x):
    shoplist.insert(i, x)


def getlast():
    return shoplist[getlen()-1]


def dividing(msg='-', times=10):
    print(msg * times)


def listout():
    for i in shoplist:
        print(i)
