# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

import pytesseract
from PIL import Image

im = Image.open(r'./pic/e.jpg')
print(pytesseract.image_to_string(im, lang='chi_sim'))
