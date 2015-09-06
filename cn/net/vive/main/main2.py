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


# print dicttest.getdict()
# print dicttest.getdict2()
# print dicttest.getdict3()


import cn.net.vive.test.dicttest as dicttest
import cn.net.vive.base.helper as helper

# dicttest.cheeseshop('Limburger', "It's very runny, sir.",
#                     "It's really very, VERY runny, sir.",
#                     shopkeeper='Michael Palin',
#                     client="John Cleese",
#                     sketch="Cheese Shop Sketch")


# dicttest.varargs('wjh', ',', 'hebei', 'beijing', 'shanghai')
# helper.dividing()

# 测试1
# args = [3,6]
# dicttest.args2(*args)

# helper.dividing()

# 测试2
# d = {'volate': 'volate1', 'state': 'state1', 'action': 'action1'}
# dicttest.parrot(**d)
import cn.net.vive.test.rececletest as rececle
test = rececle.test
# test()
# print rececle.appid


s = 'hello world'
print str(s),str(1.0/7.0),repr((1.0/7.0))
print '{0}-{1}-{other}'.format(str(5).zfill(5),str(2).zfill(8),other='sssss')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print "Jack:{Jack:d} Sjoerd:{Sjoerd:d}".format(**table)

import json
print json.dumps(table)
import os
filename = os.getcwd() + "\\test.txt"

def readfile():
    fp = open(filename,'r')
    # str1 = fp.readline()
    # str2 = fp.readline()
    lines = fp.readlines()
    for line in lines:
        print line

    fp.close()


def readfile2():
    fp = open(filename,'r')
    line = fp.readline()
    while line:
        print line
        line = fp.readline()

    fp.close()


def readfile3():
    fp = open(filename,'r')
    line = fp.readall()
    print line
    fp.close()


readfile()

quit()
