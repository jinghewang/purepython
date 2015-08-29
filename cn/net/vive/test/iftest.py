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


def guessnumber():
    number =25
    num =1
    running = True
    while num < 10 and running:
        print u"你第", num, u"次猜测"
        inputnumber = int(raw_input(u"请输入一个数字："))
        if inputnumber < 25:
            print u"你输入数字小于那个数"
        elif inputnumber > 25:
            print u"你输入数字大于那个数"
        else:
            print u"你输入数字等于那个数，你太聪明了"
            running = False

        num = num+ 1
        sleep(1)


def guessnumber2():
    number =25
    num =1
    running = True
    while num < 10 and running:
        print u"你第", num, u"次猜测"
        inputnumber = int(raw_input(u"请输入一个数字："))
        if inputnumber < 25:
            print u"你输入数字小于那个数，请重新输入:"
        elif inputnumber > 25:
            print u"你输入数字大于那个数，请重新输入:"
        else:
            print u"你输入数字等于那个数，你太聪明了"
            num = 10;running=False

        num = num+ 1
        sleep(2)