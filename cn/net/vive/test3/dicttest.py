# file:
# coding:utf-8

__author__ = 'robin'


def getempty_dict():
    return dict();


def getdictbymap():
    return {'one': 1, "two": 2, "three": 3}


def getdict3():
    return dict(one=1, two=2, three=3)


def getdict4():
    return dict(zip('one', 'two', 'three'), [1, 2, 3])


def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg

    print '*'*40
    keys = sorted(keywords.keys())
    for key in keys:
        print key,'=',keywords[key]


