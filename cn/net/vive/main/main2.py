# file:main2.py
# coding:utf-8

__author__ = 'robin'

# dir
# a = 5 ; b = 6 ;
# print dir()
# del a
# print dir()

# import cn.net.vive.test3.using_list as ulist
# print ulist.getlen()
# ulist.listout()
# print('first is:',ulist.getfirst())
# print('last is:',ulist.getlast())
# ulist.sort()
# ulist.listout()
#
# ulist.append("qqqq")
# ulist.listout()
#
# ulist.dividing()
# ulist.insert(1,'insert')
# ulist.listout()
#
# ulist.dividing()
# ulist.delfirst()
# print('first is:',ulist.getfirst())
#



def f(a, L=[]):
    L.append(a)
    return L


def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# print f(1)
# print f(2)
# print f(3)

# print f2(1)
# print f2(2)
# print f2(3)


import cn.net.vive.test3.dicttest as dicttest
# print dicttest.getdict()
# print dicttest.getdict2()
# print dicttest.getdict3()


import cn.net.vive.test3.dicttest as dicttest
import cn.net.vive.base.helper as helper

dicttest.cheeseshop('Limburger', "It's very runny, sir.",
                    "It's really very, VERY runny, sir.",
                    shopkeeper='Michael Palin',
                    client="John Cleese",
                    sketch="Cheese Shop Sketch")


dicttest.varargs('wjh', ',', 'hebei', 'beijing', 'shanghai')

helper.dividing()

# 测试1
args = [3,6]
dicttest.args2(*args)

helper.dividing()

# 测试2
d = {'volate': 'volate1', 'state': 'state1', 'action': 'action1'}
dicttest.parrot(**d)


