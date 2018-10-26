# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

import threading

lock = threading.Lock()
balance = 0
threadlocal = threading.local()


def change_it(x):
    global balance
    print('<threadname - %s , local - %s>' % (threading.current_thread().name, threadlocal.num))
    lock.acquire()
    try:
        balance = balance + x
        balance = balance - x
    finally:
        lock.release()


def run_thread(x):
    threadlocal.num = x
    for i in range(5):
        change_it(x)


print('thread (%s) is running' % threading.current_thread().name)
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
print('end')
