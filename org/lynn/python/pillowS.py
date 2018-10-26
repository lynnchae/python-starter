# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

from PIL import Image

image = Image.open('image.jpg')
w, h = image.size
print('before resize ( w:%s, h:%s)' % (w, h))

image.thumbnail((w // 2, h // 2))

print('resized to ( w:%s, h:%s)' % (w // 2, h // 2))
image.save('imagehalf.jpg', 'jpeg')
