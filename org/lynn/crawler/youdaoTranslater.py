# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import time

__author__ = 'Cailinfeng'
import json
from urllib import request, parse
import hashlib

if __name__ == '__main__':
    '''
        有道翻译：2018-10-30 可用
    '''
    totrans = input('翻译：')
    starttime = time.time()
    trans_url = 'http://fanyi.youdao.com/translate'
    form_data = {}

    u = 'fanyideskweb'
    f = str(int(round(time.time() * 1000)) + random.randint(1, 10))
    c = '6x(ZHw]mwzX#u0V7@yfwK'
    sign = hashlib.md5((u + totrans + f + c).encode('utf-8')).hexdigest()
    form_data['i'] = totrans
    form_data['from'] = 'AUTO'
    form_data['to'] = 'AUTO'
    form_data['smartresult'] = 'dict'
    form_data['client'] = 'fanyideskweb'
    form_data['salt'] = f
    form_data['sign'] = sign
    form_data['doctype'] = 'json'
    form_data['version'] = '2.1'
    form_data['keyfrom'] = 'fanyi.web'
    form_data['action'] = 'FY_BY_CLICKBUTTION'
    form_data['typoResult'] = False
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
               'Connection': 'keep-alive',
               'Content-Length': '218',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Host': 'fanyi.youdao.com',
               'Origin': 'http://fanyi.youdao.com',
               'Referer': 'http://fanyi.youdao.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
               'X-Requested-With': 'XMLHttpRequest'}

    # 使用urlencode方法转换标准格式
    data = parse.urlencode(form_data).encode('utf-8')
    # 传递Request对象和转换完格式的数据
    response = request.urlopen(trans_url, data)
    # 读取信息并解码
    html = response.read().decode('utf-8')
    # 使用JSON
    translate_results = json.loads(html)
    # 找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']
    # 打印翻译信息
    endtime = time.time()
    print("翻译结果：%s" % translate_results)
    print("[%.3f s]" % ((endtime-starttime)))
