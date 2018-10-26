# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

from multiprocessing import Pool
import os, random, time


def long_time_task(name):
    print('long time task begin : %s (%s)' % (name, os.getpid()))
    starttime = time.time()
    time.sleep(random.random() * 3)
    endtime = time.time()
    print('pool process %s (%s) end , expend %.2f' % (name, os.getpid(), (endtime - starttime)))


if __name__ == '__main__':
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=('process' + str(i),))
    p.close()
    # close()后，pool不可以再添加线程
    p.join()
    print('main process end')
