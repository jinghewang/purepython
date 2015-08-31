# file:iftest.py
# coding:utf-8

__author__ = 'robin'

from time import sleep

def iftest():
    number = 10
    guess = int(raw_input(u"请输入一个数字："))

    print u"正在处理，请稍等..."
    sleep(3)

    if guess == number:
        print u"guess 等于 number"
        print "<<<"
    elif guess < number:
        print u"guess 小于 number"
        print "<<<<<"
    else:
        print u"guess 大于 number"

    print u"处理完成"
