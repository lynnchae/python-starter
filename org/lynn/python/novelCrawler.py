# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

import sys, time, os, requests
from bs4 import BeautifulSoup

domain = 'https://www.biqukan.com'
novel_fanren = 'https://www.biqukan.com/3_3050/'
novel_chaper_urls = []
nums = 0


class Novel(object):

    def __init__(self, novel_chapter_url):
        self.novel_chapter_url = novel_chapter_url

    def get_novel_content(self):
        req = requests.get(url=self.novel_chapter_url)
        html = req.content
        bf = BeautifulSoup(html, features="html.parser")
        texts = bf.find_all('div', attrs={'class': 'showtxt'})
        self.title = bf.find_all('h1')[0].text
        self.content = texts[0].text.replace(' ', '\n').replace('\xa0' * 8, '\n')

    def save(self):
        self.get_novel_content()
        with open('./txt/' + self.title + '.txt', 'a', encoding='utf-8') as f:
            f.writelines(self.content)
            f.write('\n\n')


class Novels(object):

    def __init__(self, novel_url):
        req = requests.get(url=novel_url)
        div_bf = BeautifulSoup(req.content, features="html.parser")
        div = div_bf.find_all('div', attrs={'class': 'listmain'})
        a_bf = BeautifulSoup(str(div[0]), features="html.parser")
        a = a_bf.find_all('a')
        global nums
        nums = a[12:]
        for each in a[12:22]:
            novel_chaper_urls.append(domain + each.get('href'))
        nums = len(novel_chaper_urls)


def progress(percent, width=50):
    '''进度打印功能'''
    if percent >= 100:
        percent = 100
    show_str = ('[%%-%ds]' % width) % (int(width * percent / 100) * "#")  # 字符串拼接的嵌套使用
    sys.stdout.write('\r%s %d%%' % (show_str, percent))
    sys.stdout.flush()


if __name__ == '__main__':
    for x in [z for z in os.listdir('./txt/') if os.path.isfile('./txt/'+z) and os.path.splitext(z)[1] == '.txt']:
        os.remove('./txt/' + x)
    print('《凡人修仙传》前十章开始下载：')
    time.sleep(20)
    Novels(novel_fanren)
    for index, url in enumerate(novel_chaper_urls):
        novel = Novel(url)
        novel.save()
        progress(int(100 * (index + 1) / nums), width=30)
    print('\n')
    print('《凡人修仙传》前十章下载完成')
