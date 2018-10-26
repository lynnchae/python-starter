# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

from contextlib import contextmanager,closing
from urllib.request import urlopen

class Query(object):

    def query(self):
        print('select from table with result')


@contextmanager
def connect_close():
    print('connecting to db...')
    yield Query()
    print('close connect')

with connect_close() as q:
    q.query()

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)