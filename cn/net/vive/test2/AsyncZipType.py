# file:
# coding:utf-8

__author__ = 'robin'


import threading
import zipfile


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

