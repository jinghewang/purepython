# file:lambdatest.py
# coding:utf-8

__author__ = 'robin'

import cn.net.vive.base.helper as helper
import cn.net.vive.test3.dicttest as dicttest

helper.dividing()

f = dicttest.make_incrementor(42)
print f(0)
print f(1)

helper.dividing()
pairs = [(1,'one'),(2,'two'),(3,'three')]
pairs.sort(key=lambda pair:pair[1])
print pairs

helper.dividing()
alist = range(1, 10)
low = 3;
high = 6
print filter(lambda x: low < x < high, alist)

helper.dividing()
def with_bound(value, l=low, h=high):
    return l < value < h;

print filter(with_bound,alist)
