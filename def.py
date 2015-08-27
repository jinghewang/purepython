__author__ = 'robin'


def outputsth(sth):
    return sth + 5


def floor(number):
    result = 0
    while result <= number:
        result = result + 1
    result = result - 1
    return result

def sum(x,y):
    return x+y;


print outputsth(2)
print floor(5);
print sum(3,5)
