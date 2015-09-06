# file:
# coding:utf-8

__author__ = 'robin'

import cn.net.vive.base.helper as helper


def test():
    # collection
    ls = [1,2,3,4,5,3]
    c = set(ls)
    print c

    print 3 in c
    a = set('abracadabra')
    b = set('alacazam')
    # letters in a but not in b
    print a-b
    # letters in either a or b
    print a|b
    # letters in both a and b
    print a & b
    # letters in a or b but not both
    print a ^ b

    print [x for x in set('abcd') if x not in 'ab']



    ls = []
    for i in range(0,10):
        ls.append(i**2)

    helper.print2(ls,True)

    # for x
    ls2 = [x**2 for x in range(0,10)]
    helper.print2(ls2,True)

    # map
    ls2 = map(lambda x:x**2,range(0,10))
    helper.print2(ls2,True)

    # for x,y
    ls2 = [(x,y) for x in[1,2,3] for y in[1,2,3] if x != y]
    helper.print2(ls2,True)

