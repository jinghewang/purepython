# file:
# coding:utf-8

__author__ = 'robin'

import cn.net.vive.test3.using_list as ulist
import cn.net.vive.test.dicttest as dicttest
import cn.net.vive.base.helper as helper


def test():
    # test-1
    print ulist.getlen()
    ulist.listout()
    print('first is:', ulist.getfirst())
    print('last is:', ulist.getlast())
    ulist.sort()
    ulist.listout()

    ulist.append("qqqq")
    ulist.listout()

    ulist.dividing()
    ulist.insert(1, 'insert')
    ulist.listout()

    ulist.dividing()
    ulist.delfirst()
    print('first is:', ulist.getfirst())

    # test-2
    dicttest.cheeseshop('Limburger', "It's very runny, sir.",
                        "It's really very, VERY runny, sir.",
                        shopkeeper='Michael Palin',
                        client="John Cleese",
                        sketch="Cheese Shop Sketch")
    dicttest.varargs('wjh', ',', 'hebei', 'beijing', 'shanghai')
    helper.dividing()

    print dicttest.getdict()
    print dicttest.getdict2()
    print dicttest.getdict3()


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
