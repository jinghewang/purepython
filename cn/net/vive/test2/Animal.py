# file:Animal.py
# coding:utf-8

__author__ = 'robin'


class Animal:
    """
    A simple example class
    """

    def __init__(self):
        pass

    i = 12345
    msg = 'hello world'

    def f(self):
        global msg
        return msg
