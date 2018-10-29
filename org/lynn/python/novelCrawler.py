# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

from bs4 import BeautifulSoup
import requests

domain = 'https://www.biqukan.com'
novel_fanren = 'https://www.biqukan.com/3_3050/'
novels = []
nums = 0


class Novel(object):

    def __init__(self, novel_url):
        self.novel_url = novel_url

    def get_novel_content(self):
        req = requests.get(url=self.novel_url)
        html = req.content
        bf = BeautifulSoup(html, features="html.parser")
        texts = bf.find_all('div', attrs={'class': 'showtxt'})
        self.title = bf.find_all('h1')[0].text
        self.content = texts[0].text.replace(' ', '\n').replace('\xa0' * 8, '\n')

    def save(self):
        self.get_novel_content()
        with open('./txt/' + self.title + '.txt', 'w', encoding='utf-8') as f:
            f.writelines(n.content)
            f.write('\n\n')


def get_all_novels(novel):
    req = requests.get(url=novel)
    div_bf = BeautifulSoup(req.content, features="html.parser")
    div = div_bf.find_all('div', attrs={'class': 'listmain'})
    a_bf = BeautifulSoup(str(div[0]), features="html.parser")
    a = a_bf.find_all('a')
    global nums
    nums = a[12:]
    for each in a[12:22]:
        novel = Novel(domain + each.get('href'))
        yield novel


if __name__ == '__main__':
    print('《凡人修仙传》前十章开始下载：')
    for n in get_all_novels(novel_fanren):
        n.save()
    print('《凡人修仙传》前十章下载完成')
