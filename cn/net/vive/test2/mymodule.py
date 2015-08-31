# file:mymodule.py
# coding:utf-8


__author__ = 'robin'

version = 'v0.87'


def sayhay(msg='wjh'):
    """say hay tsh

    say say sth sth
    :param msg:
    """
    print 'hello:', msg


def modulename():
    return __name__


if __name__ == "__main__":
    sayhay('wwwww')

print(sayhay.__doc__)