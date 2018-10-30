# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

from urllib import request
import subprocess as sp
import re


if __name__ == '__main__':
    cmd = "ping -n 3 -w 3 127.0.0.1"
    #执行命令
    p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    #获得返回结果并解码
    out = p.stdout.read().decode("gbk")
    lose_time = re.compile(u"丢失 = (\d+)", re.IGNORECASE)
    lose_time = lose_time.findall(out)
    print(lose_time)

#
# if __name__ == "__main__":
#     #访问网址
#     url = 'http://www.whatismyip.com.tw/'
#     #这是代理IP
#     proxy = {'http':'106.46.136.112:808'}
#     #创建ProxyHandler
#     proxy_support = request.ProxyHandler(proxy)
#     #创建Opener
#     opener = request.build_opener(proxy_support)
#     #添加User Angent
#     opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
#     #安装OPener
#     request.install_opener(opener)
#     #使用自己安装好的Opener
#     response = request.urlopen(url)
#     #读取相应信息并解码
#     html = response.read().decode("utf-8")
#     #打印信息
#     print(html)