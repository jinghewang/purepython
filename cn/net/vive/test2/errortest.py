# file:
# coding:utf-8

__author__ = 'robin'


def test():
    import sys
    from time import sleep
    import cn.net.vive.test2.MyError as MyError

    while True:
        try:
            val = raw_input("Please enter a number: ")
            if not val.isdigit():
                raise TypeError('type-error=' + val)

            val = int(val)
            if 10 < val < 20:
                raise ValueError('value-error=' + str(val))
            elif 20 <= val < 30:
                raise KeyError('key-error=' + str(val))
            elif val >= 30:
                raise MyError('MyError=' + str(val))
            else:
                pass

            sleep(1)
            # break;
        except ValueError as e:
            print 'value error:' + e.message
        except TypeError as e:
            print 'type error:' + e.message
        except:
            print "Unexpected error:", sys.exc_info()[0]
            # raise
        finally:
            print '---done---'
