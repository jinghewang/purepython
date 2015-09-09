# file:
# coding:utf-8

__author__ = 'robin'

# 11. 标准库概览 — 第II部分

import cn.net.vive.base.helper as helper


def test():
    helper.dividing_with_title(' start ')

    # repr
    import repr
    print repr.repr(set('abcdedabc'))
    print repr.repr(dict({'name' : 'wjh', 'age' : 11}))

    # pprint
    import pprint
    t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',  'yellow'], 'blue']]]
    pprint.pprint(t,None,1,80)

    # textwrap
    import textwrap
    doc = """The wrap() method is just like fill() except that it returns
    a list of strings instead of one big string with newlines to separate
    the wrapped lines."""
    print textwrap.fill(doc,50)

    # locale
    import locale
    locale.setlocale(locale.LC_ALL,'English_United States.1252')
    conv=locale.localeconv()
    x = 1234.6
    print locale.format("%d", x, grouping=True)
    print locale.format_string("%s%.*f", (conv['currency_symbol'],      conv['frac_digits'], x), grouping=True)

    # Template
    from string import Template
    t = Template('${village}folk send $$10 to $cause.')
    print t.substitute(village='Nottingham', cause='the ditch fund')

    d = dict(name='wjh',age=20)
    t = Template('name: $name and age: $age')
    print t.substitute(d)
    print t.safe_substitute(d)

    import time, os.path
    photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
    # fmt = raw_input('Enter rename style (%d-date %n-seqnum %f-format):  ')
    # print fmt

    # struct
    import struct
    data = open(helper.getfile('test.txt'), 'rb')
    print data.readline()
    data.close()

    # thread
    import threading, zipfile

    print '--The main program continues to run in foreground.--11'
    background = AsyncZip('test.txt', 'test.zip')
    background.start()
    print '--The main program continues to run in foreground.--22'

    background.join()    # Wait for the background task to finish
    print '--Main program waited until background was done.'


    # end
    helper.dividing_with_title(' end ')


import threading, zipfile


class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
        print '>>>Init background zip of: ', self.infile

    def run(self):
        print '>>>Start background zip of: ', self.infile
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print '>>>Finished background zip of: ', self.infile

