# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

import os
from multiprocessing import Process


def run_pro(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('main process (%s) running...' % os.getpid())
    p = Process(target=run_pro, args=('childProcess',))
    print('child process will start')
    p.start()
    p.join()
    print('end')
