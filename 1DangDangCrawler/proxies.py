# from iptools import header, dict2proxy
from bs4 import BeautifulSoup as Soup
import json
import requests
import os
import numpy as np
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/64.0.3282.186 Safari/537.36'}
def parse_items(items):
    # 存放ip信息字典的列表
    ips = []
    for item in items:
        tds = item.find_all('td')
        # 从对应位置获取ip，端口，类型
        ip, port, _type = tds[1].text, int(tds[2].text), tds[5].text
        ips.append({'ip': ip, 'port': port, 'type': _type})
    return ips

def dict2proxy(dic):
    s = dic['type'] + '://' + dic['ip'] + ':' + str(dic['port'])
    return {'http': s, 'https': s}

def check_ip(ip):
    try:
        proxy = dict2proxy(ip)
        url = 'https://www.ipip.net/'
        r = requests.get(url, headers=header, proxies=proxy,timeout=5)
        r.raise_for_status()
        print(r.status_code, ip['ip'])
    except:
        return False
    else:
        return True

def get_proxies(index,need_check=False):
    path='proxies_pool.npy'
    if os.path.exists(path):
        good_proxies=np.load(path,allow_pickle=True)
        if need_check:
            good_proxies=[ip for ip in good_proxies if check_ip(ip)]
        if len(good_proxies) >2:
            return good_proxies
    url = 'http://www.xicidaili.com/nt/%d' % index
    r = requests.get(url, headers=header)
    r.encoding = r.apparent_encoding
    r.raise_for_status()
    soup = Soup(r.text, 'lxml')
    # 第一个是显示最上方的信息的，需要丢掉
    items = soup.find_all('tr')[1:]
    ips = parse_items(items)
    good_proxies = []
    for ip in ips:
        if check_ip(ip):
            good_proxies.append(ip)
    np.save(path,good_proxies)
    return good_proxies


def write_to_json(ips):
    with open('proxies.json', 'w', encoding='utf-8') as f:
        json.dump(ips, f, indent=4)

if __name__=="__main__":
    get_proxies(1)


