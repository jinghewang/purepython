# file:
# coding:utf-8

__author__ = 'robin'


# str
s = 'hello world'
print str(s),str(1.0/7.0),repr((1.0/7.0))
print '{0}-{1}-{other}'.format(str(5).zfill(5),str(2).zfill(8),other='sssss')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print "Jack:{Jack:d} Sjoerd:{Sjoerd:d}".format(**table)