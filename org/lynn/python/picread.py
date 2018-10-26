# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'


import pytesseract
from PIL import Image


im = Image.open(r'a.jpg')
print(pytesseract.image_to_string(im))