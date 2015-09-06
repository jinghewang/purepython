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


def varargs(name, separator, *others):
    """
    可变参数

    可变参数，包括名称，分隔符，参数
    :type name: str
    :type separator: str
    :type others: list
    :param name:姓名
    :param separator:分隔符
    :param others:参数
    """
    print 'name:', name
    print separator.join(others)
    return 'name',name,separator.join(others)


def args2(name,age):
    print 'name:', name, 'age:', age
    return True


def parrot(volate, state='a stiff', action='voom'):
    """
    parrot

    parrot
    :rtype : bool
    :type volate: str
    :type state: str
    :type action: str
    :param volate: volate
    :param state: state
    :param action: action
    """
    print 'volate:', volate, ' state:', state, ' action:', action
    return True


def make_incrementor(n):
    return lambda x:x+n
