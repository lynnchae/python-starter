import functools
import time


def log(func):
    @functools.wraps(func)
    def dolog(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)

    return dolog


def metric(func):
    def dometric(*args, **kw):
        starttime = time.time()
        print('execute %s() begin at %s' % (func.__name__, starttime))
        result = func(*args, **kw)
        endtime = time.time()
        print('execute %s() complete at %s' % (func.__name__, endtime))
        print('expend %s' % (endtime - starttime))
        return result
    return dometric


@metric
def testmethod(x):
    time.sleep(1)
    print(x)


testmethod('hello')
