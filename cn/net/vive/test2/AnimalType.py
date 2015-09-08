# file:Animal.py
# coding:utf-8

__author__ = 'robin'

import cn.net.vive.base.helper as helper


class Animal:
    """
    A simple example class
    """

    i = 12345
    name = ''
    hmsg = 'hello world'
    company = 'vive'

    def __init__(self, name=''):
        self.name = name

    def list_keys(self):
        """
        显示实例的所有函数及变量
        """
        m1 = [{'method': method, 'callable': callable(getattr(self,method)), 'value': None} for method in dir(self) if callable(getattr(self,method))]
        m2 = [{'method': method, 'callable': callable(getattr(self,method)), 'value': getattr(self, method)} for method in dir(self) if (not callable(getattr(self,method))) and not method.startswith('__')]
        print m1
        print m2

    def readme(self):
        helper.dividing_with_title('readme start')
        print self.__module__
        print self.__class__
        print self.__doc__
        print dir(self)
        helper.dividing_with_title('readme end')

    def f(self):
        return self.hmsg

    def hello(self, msg='hello'):
        print self.company, ':', msg
