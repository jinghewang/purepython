# file:
# coding:utf-8

__author__ = 'robin'

# 11. 标准库概览 — 第II部分

import cn.net.vive.base.helper as helper


def test():
    helper.dividing_with_title(' start ')

    # repr
    import repr
    print repr.repr(set('abcdedabc'))
    print repr.repr(dict({'name' : 'wjh', 'age' : 11}))

    # pprint
    import pprint
    t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',  'yellow'], 'blue']]]
    pprint.pprint(t,None,1,80)

    # textwrap
    import textwrap
    doc = """The wrap() method is just like fill() except that it returns
    a list of strings instead of one big string with newlines to separate
    the wrapped lines."""
    print textwrap.fill(doc,50)

    # locale
    import locale
    locale.setlocale(locale.LC_ALL,'English_United States.1252')
    conv=locale.localeconv()
    x = 1234.6
    print locale.format("%d", x, grouping=True)
    print locale.format_string("%s%.*f", (conv['currency_symbol'],      conv['frac_digits'], x), grouping=True)

    # Template
    from string import Template
    t = Template('${village}folk send $$10 to $cause.')
    print t.substitute(village='Nottingham', cause='the ditch fund')

    d = dict(name='wjh',age=20)
    t = Template('name: $name and age: $age')
    print t.substitute(d)
    print t.safe_substitute(d)

    import time, os.path
    photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
    # fmt = raw_input('Enter rename style (%d-date %n-seqnum %f-format):  ')
    # print fmt

    # struct
    import struct
    data = open(helper.getfile('test.txt'), 'rb')
    print data.readline()
    data.close()


def test_thread():
    # thread
    from cn.net.vive.test2.AsyncZipType import AsyncZip

    print '-->The main program continues to run in foreground.'
    background = AsyncZip('test.txt', 'test.zip')
    background.start()

    background.join()    # Wait for the background task to finish
    print '-->Main program waited until background was done.'

    # end
    helper.dividing_with_title(' end ')


def test_weakref():
    import weakref,gc
    from cn.net.vive.test2.AType import A
    a = A(10)
    d = weakref.WeakValueDictionary()
    d['primary'] = a
    print d['primary']
    del a
    gc.collect()
    print d['primary']


def test_log():
    import logging
    logging.debug("debug")
    logging.info("info")
    logging.warning("warn")
    logging.error("error")
    logging.critical("critical")


def test_list():
    # array
    from array import array
    a = array('H',[4000,10,700,22222])
    print sum(a)
    print a[1:3]

    # collection
    from collections import deque
    d = deque(['task1','task2','task3'])
    d.append('task4')
    print 'handing',d.popleft()

    # bisect
    import bisect
    scores = [(100,'wjh'),(200,'lht'),(400,'lvkui')]
    bisect.insort(scores,(300,'www'))
    print scores

    # heapq
    from heapq import heappop,heappush,heapify
    data = [1,3,5,7,6,2]
    heapify(data)
    heappush(data,-5)
    print [heappop(data) for i in range(3)]

    # decimal
    from decimal import *
    x = Decimal(0.70)* Decimal(1.05)
    print x, x.quantize(Decimal('0.01')),round(.70 * 1.05, 2)

    getcontext().prec = 36
    print Decimal(1) / Decimal(7)








