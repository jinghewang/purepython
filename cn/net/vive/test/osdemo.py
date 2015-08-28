# file:osdemo.py
# coding:utf-8

__author__ = 'robin'


def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isexist = os.path.exists(path)

    if not isexist:
        print path, u'目录创建成功'
        os.makedirs(path)
        return True
    else:
        print path, u'目录已经存在'
        return False