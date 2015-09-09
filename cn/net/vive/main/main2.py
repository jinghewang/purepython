# file:main2.py
# coding:utf-8

__author__ = 'robin'



import os

print os.getcwd()
# print os.system("mkdir '123-456'")
# print dir(os)
# print help(os)

import shutil
# shutil.copyfile()
# shutil.move()

import glob
print glob.glob("*.py")

import sys
print sys.argv
print sys.stderr.write('warning error')

import re
print re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print 'tea for too'.replace('tea','coffee')

import math
print math.pi
print math.ceil(1.05)

import random
print random.choice(range(1,10))
print random.choice(['ww','zz'])
print random.random()
print random.randrange(6)

import urllib,urllib2,urlparse
# for line in urllib2.urlopen('https://www.baidu.com/'):
#    print line

import smtplib


from datetime import date
print date.today()
print date.today().strftime('%m-%d-%y')

birthday = date(2015,10,1)
age = date.today()-birthday
print age

print '*'*20

import zlib
s = 'witch which has which witches wrist watch'
print len(s)
t = zlib.compress(s)
print len(t)

print zlib.decompress(t)
print zlib.crc32(s)


from timeit import Timer
print Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print Timer('a,b = b,a', 'a=1; b=2').timeit()


quit()

# dir
# a = 5 ; b = 6 ;
# print dir()
# del a
# print dir()

# 测试1
# args = [3,6]
# dicttest.args2(*args)

# helper.dividing()

# 测试2
# d = {'volate': 'volate1', 'state': 'state1', 'action': 'action1'}
# dicttest.parrot(**d)

# 循环测试
# import cn.net.vive.test.rececletest as rececle
# test = rececle.test
# test()
# print rececle.appid

# json 测试
import cn.net.vive.test.jsontest as jsontest
jsontest.test()

quit()
