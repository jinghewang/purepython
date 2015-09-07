# file:
# coding:utf-8

__author__ = 'robin'


import json
import cn.net.vive.base.helper as helper

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
filename = helper.getfile("test.txt")


def test():
    # 查看 json
    # print json.dumps(table)

    # 导出json
    # dumpfile()

    # 加载json
    loadfile()

    # 读取文件
    # readfile2()


def loadfile():
    fp = open(filename,'r')
    memo = json.load(fp)
    print memo
    for k, v in memo.iteritems():
        print k, v
    fp.close()


def dumpfile():
    fp = open(filename,'w')
    json.dump(table,fp)
    fp.close()


def readfile():
    fp = open(filename,'r')
    lines = fp.readlines()
    for line in lines:
        print line

    fp.close()


def readfile2():
    fp = open(filename,'r')
    line = fp.readline()
    while line:
        print line
        line = fp.readline()

    fp.close()


def readfile3():
    fp = open(filename,'r')
    line = fp.readall()
    print line
    fp.close()



