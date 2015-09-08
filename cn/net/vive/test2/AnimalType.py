# file:Animal.py
# coding:utf-8

__author__ = 'robin'

import cn.net.vive.base.helper as helper

class Animal:
    """
    A simple example class
    """

    def __init__(self):
        pass

    i = 12345
    hmsg = 'hello world'
    company = 'vive'

    def readme(self):
        helper.dividing_with_title('readme start')
        print self.__module__
        print self.__class__
        print self.__doc__
        helper.dividing_with_title('readme end')

    def f(self):
        return self.hmsg

    def hello(self, msg='hello'):
        print self.company, ':', msg
