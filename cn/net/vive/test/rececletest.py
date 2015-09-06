# file:
# coding:utf-8

__author__ = 'robin'

appid = 'v.87'

import cn.net.vive.base.helper as helper


def test():
    # 循环遍历
    helper.dividing()
    for i, v in enumerate(['one', 'two', 'three']):
        print i, v

    helper.dividing()
    for i, v in enumerate([x ** 2 for x in range(0, 5)]):
        print i, v

    helper.dividing()
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):
        print f

    helper.dividing()
    for v in basket:
        print v

    helper.dividing()
    for i, v in enumerate(basket):
        print i, v

    # zip
    helper.dividing()
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q,a in zip(questions,answers):
        print 'What is your {0}?  It is {1}.'.format(q, a)


    helper.dividing()
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k,v in knights.iteritems():
        print k,v


    # 切片
    words = ['cat','window','difference']
    for w in words[:]:
        if  len(w)>6:
            words.insert(0,w)

    print words
