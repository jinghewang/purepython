# file:
# coding:utf-8

__author__ = 'robin'





#encoding:UTF-8
import urllib, urllib2, cookielib, socket

url = "http://www.baidu.com"
data = urllib.urlopen(url).read()
# data = data.decode('UTF-8')
print(data)
