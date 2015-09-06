# file:
# coding:utf-8

__author__ = 'robin'


def test():
    # set
    tel = {'id':'1','name':'wjh','age':'20'}
    print tel.get('name'),tel['age']
    del tel['age']
    print tel
    print tel.keys()
    print 'name' in tel

    ls2 = sorted(tel, lambda x, y: cmp(len(x), len(y)),None,True)
    print ls2

    ls2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print ls2

    print {x: x ** 2 for x in range(1, 5)}

    print dict(sape=4139, guido=4127, jack=4098)
