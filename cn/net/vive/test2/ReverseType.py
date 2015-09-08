# file:
# coding:utf-8

__author__ = 'robin'

def test():
    # next实现
    r = Reverse('spam')
    # iter(r)
    for char in r:
        print char

    # 生成器
    for c in reverse('glof'):
        print c

    print sum([x for x in range(1,5)])
    print sum(x for x in range(1,5))

    xvec = ['w','l','z']
    yvec = [1,2,3]
    print [(x,y) for x,y in zip(xvec,yvec)]

    print set(n for n in range(1,6))
    print max(n for n in range(1,7))

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

class Reverse:
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration()
        self.index = self.index - 1
        return self.data[self.index]