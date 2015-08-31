# file:whiletest.py
# coding:utf-8

__author__ = 'robin'

from time import sleep


def whiletest():
    num = 1
    max = 5
    while True:
        # break
        if num > max:
            print u"你已经猜测", max, u"次，下次再努力"
            break

        # input
        print u"输入次数为：",num
        inputnumber = int(raw_input(u"请输入一个数字："))

        # continue
        if  inputnumber < 0:
            print u"你输入了一个不合法数据，此次输入忽略"
            continue;

        # break2
        if inputnumber == 10:
            print(u"你好聪明")
            break
        else:
            print u"你输入数字不正确，请再次输入"

        num += 1
    else:
        print "while-else"


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
    else:
        print u"这里是 while-else"


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