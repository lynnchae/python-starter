import requests
from bs4 import BeautifulSoup
import time,random
import re,sys


def analyze_ip():
    ipurl ='https://www.ip.cn/index.php?ip='
    ipaddfile = open('./ipadd.txt','a')
    with open('ip.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip('\n')
            if line:
                ipdataarr = re.split(r',',line)
                ip = ipdataarr[0]
                firstVisitDate = ipdataarr[1]
                firstVisitTime = ipdataarr[2]
                req = requests.get(url=ipurl+ip)
                html = req.content
                bf = BeautifulSoup(html, features="html.parser")
                time.sleep(random.random() * 2)
                texts = bf.find_all('code')
                ipaddfile.writelines('date: %s, time: %s, ip: %s, address: %s ' % (firstVisitDate,firstVisitTime,ip,texts[1].get_text()))
                ipaddfile.writelines('\n')
    ipaddfile.close()

if __name__ == '__main__':
    analyze_ip()