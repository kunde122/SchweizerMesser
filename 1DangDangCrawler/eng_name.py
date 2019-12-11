# -*- coding:utf-8 -*-
import urllib.request
import time
import csv
import codecs
import regex as re
from bs4 import BeautifulSoup
from proxies import get_proxies
import pandas as pd
import random
# def my_fun(a,b={}):
#     print(a)
#     b['ds']=1
# my_fun(2,id=10)

def get_bs(url,headers,proxies=None):
    # 代理, 如果在需要代理就加上这行代码
    # proxies={'http':'183.136.177.77:3128'}
    if proxies:
        proxy_handler = urllib.request.ProxyHandler(proxies)
        opener = urllib.request.build_opener(proxy_handler)
        urllib.request.install_opener(opener)

    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response)
    return soup

def dict2proxy(dic):
    s = dic['type'] + '://' + dic['ip'] + ':' + str(dic['port'])
    return {'http': s, 'https': s}

def dict2proxy2(dic):
    s = dic['ip'] + ':' + str(dic['port'])
    return {'http': s}

def main():
    # 爬取地址, 当当所有 Python 的书籍, 一共是 21 页
    url = "http://en-name.xiao84.com/changjian/"
    # url='https://search.jd.com/Search?keyword=python&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=python&page=5&s=104&click=0'
    # url='https://search.jd.com/Search?keyword=python&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=python&page=5&s=104&click=0'
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    ip_list=get_proxies(1,need_check=True)
    page=1


    data=[]
    while True:

        try:
            #省url
            page_url = 'http://en-name.xiao84.com/changjian/p{}.html'.format(page)

            proxy = dict2proxy2(random.choice(ip_list))
            soup = get_bs(page_url, headers, proxy)
            names = soup.find_all('td', class_='en-col')
            for item in names:
                enname = item.find('a', class_='enname').get_text()
                print(enname)
                data.append(enname)
            page += 1
        except:
            break
    with open('eng_names1.txt','w') as fout:
        for name in data:
            fout.write(name+'\n')


    # 代理, 如果在需要代理就加上这行代码
    # proxy_handler = urllib.request.ProxyHandler({
    #
    # })
    # opener = urllib.request.build_opener(proxy_handler)
    # urllib.request.install_opener(opener)



def parse_content(response):
    # 提取爬取内容中的 a 标签, 例如：
    # <a
    #     class="pic" dd_name="单品图片"
    #     ddclick="act=normalResult_picture&amp;pos=23648843_53_2_q"
    #     href="http://product.dangdang.com/23648843.html"
    #     name="itemlist-picture"
    #     target="_blank" title="
    #     趣学Python――教孩子学编程 ">
    #
    #   <img
    #       alt=" 趣学Python――教孩子学编程 "
    #       data-original="http://img3x3.ddimg.cn/20/34/23648843-1_b_0.jpg"
    #       src="images/model/guan/url_none.png"/>
    # </a>
    soup = BeautifulSoup(response)
    # temps = soup.find_all('a',attrs={'name':"itemlist-picture"})
    # temps = soup.find_all(lambda x:x.has_attr('title'))

    temps = soup.find('p',attrs={'name':'title'})
    global books
    books = books + temps
    print('get books size = ' + str(len(books)))


def show_result():
    file_name = 'PythonBook.csv'
    file_name = 'PythonBook_my.csv'

    # 指定编码为 utf-8, 避免写 csv 文件出现中文乱码
    with codecs.open(file_name, 'w', 'utf-8') as csvfile:
        filednames = ['书名', '页面地址', '图片地址']
        writer = csv.DictWriter(csvfile, fieldnames=filednames)

        writer.writeheader()
        for book in books:
            print(book)
            # print(book.attrs)
            # 获取子节点<img>
            # (book.children)[0]
            if len(list(book.children)[0].attrs) == 3:
                img = list(book.children)[0].attrs['data-original']
            else:
                img = list(book.children)[0].attrs['src']

            try:
                writer.writerow({'书名':book.attrs['title'], '页面地址':book.attrs['href'], '图片地址': img})
            except UnicodeEncodeError:
                print("编码错误, 该数据无法写到文件中, 直接忽略该数据")

    print('将数据写到 ' + file_name + '成功！')


if __name__ == '__main__':
    books = []
    main()


