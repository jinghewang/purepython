# file:using_list.py
# coding:utf-8

__author__ = 'robin'


shoplist = ["apple","bear","banana"]


def getlen():
    return len(shoplist)


def getfirst():
    return shoplist[0]


def delfirst():
    del shoplist[0]


def sort():
    shoplist.sort()


def getlast():
    return shoplist[getlen()-1]


def listout():
    for i in shoplist:
        print(i)
