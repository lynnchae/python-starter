# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

from contextlib import closing
from enum import Enum, unique
import requests, os


@unique
class Category(Enum):
    Wallpapers = 'collections/1065976'
    TexturesPatterns = 'collections/3330445'
    Nature = 'collections/3330448'
    CurrentEvents = 'collections/3356631'
    Architecture = 'collections/3348849'
    Animals = 'collections/3330452'
    Travel = 'collections/3356570'
    ArtsCulture = 'collections/3330461'


class UnsplashCrawler(object):

    def __init__(self, download_size=25, catory=Category.Architecture):
        # nature category download url
        self.pic_json_url = ('https://unsplash.com/napi/xxx/photos?page=1&per_page=' + str(
            download_size) + '&order_by=latest').replace('xxx', catory.value)
        self.down_url = 'https://unsplash.com/photos/xxx/download?force=true'

    def get_pic_ids(self):
        req = requests.get(self.pic_json_url)
        self.ids = []
        for x in req.json():
            self.ids.append(x['id'])

    def download_pic(self):
        self.get_pic_ids()
        for index, id in enumerate(self.ids):
            print('downloading the No.%d picture' % (index + 1))
            url = self.down_url.replace('xxx', id)
            with closing(requests.get(url=url, stream=True, verify=False)) as r:
                if not os.path.exists('./pic'):
                    os.mkdir('./pic')
                with open('./pic/%s.jpg' % ('unsplash_' + id), 'ab+') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            f.flush()


if __name__ == '__main__':
    unsplashCrawler = UnsplashCrawler(download_size=10, catory=Category.Nature)
    unsplashCrawler.download_pic()
