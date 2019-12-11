# -*- coding:utf-8 -*-
import urllib.request
import time
import csv
import codecs
import regex as re
from bs4 import BeautifulSoup
import json
import pandas as pd
# def my_fun(a,b={}):
#     print(a)
#     b['ds']=1
# my_fun(2,id=10)


def main():
    res=pd.read_csv('card_infos.tsv', sep='\t')
    res.to_excel('card_infos1.xlsx', index=False)
    wechat_app()
    # 爬取地址, 当当所有 Python 的书籍, 一共是 21 页
    url = "http://search.dangdang.com/?key=python&act=input&show=big&page_index="
    # url='https://search.jd.com/Search?keyword=python&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=python&page=5&s=104&click=0'
    url='https://search.jd.com/Search?keyword=python&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=python&page=5&s=104&click=0'
    url='https://search.jd.com/Search?keyword=python&enc=utf-8&wq=python&pvid=59e126cd284e439283ad40fbe2132160'
    # url='https://list.youku.com/category/show/c_96_s_6_g_%E7%A7%91%E5%B9%BB.html?spm=a2ha1.12701310.app.5~5!2~5!2~5~5~DL!3~DD~A!5'
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }

    # 代理, 如果在需要代理就加上这行代码
    # proxy_handler = urllib.request.ProxyHandler({
    #
    # })
    # opener = urllib.request.build_opener(proxy_handler)
    # urllib.request.install_opener(opener)

    index = 1
    while index <= 1:
        # 发起请求
        url='https://wxapp.daqinjia.cn/wx/api/qcard/v1/card/cardinfo/?card_id=213672'
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        index = index + 1
        # 解析爬取内容
        parse_content(response)
        time.sleep(1)  # 休眠1秒

    show_result()

def wechat_app():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    headers={'charset': 'utf-8',
            'authorization': 'CardToken 816c94f604002ace42676f16e4058a0bd1cbb71b',
            'referer': 'https://servicewechat.com/wxbe180eb22e785877/6/page-frame.html',
             'app-id': 'wxbe180eb22e785877',
             'content-type': 'application/json',
             'accept': 'application/json',
             'User-Agent': 'Mozilla/5.0 (Linux; Android 9; COR-AL00 Build/HUAWEICOR-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 MicroMessenger/6.7.2.1340(0x2607023A) NetType/WIFI Language/zh_CN',
             'Host': 'wxapp.daqinjia.cn',
             #--compressed 'https://wxapp.daqinjia.cn/wx/api/qcard/v1/group/?page=1&app_id=wxbe180eb22e785877'
    }

    groups=['G6P6f4vI_DzZx2M--3qTN7Tf0rjA']
    url = 'https://wxapp.daqinjia.cn/wx/api/qcard/v1/card/cardinfo/?card_id=197758'
    #此网址不能在火狐浏览器直接访问，不知道为什么？
    # url='https://wxapp.daqinjia.cn/wx/api/qcard/v1/group/cards/?group_id=G6P6f4vI_DzZx2M--3qTN7Tf0rjA&page=15&app_id=wxbe180eb22e785877'
    get_detail_info(headers)
    # for group_id in groups:
    #     get_group_info(group_id,headers)
    print(0)

def get_group_info(group_id,headers):
    group_url = 'https://wxapp.daqinjia.cn/wx/api/qcard/v1/group/cards/?group_id={}&page={}&app_id=wxbe180eb22e785877'.format(group_id,'{}')
    page=1
    card_ids=[]
    while True:

        try:
            page_url=group_url.format(page)
            request = urllib.request.Request(url=page_url, headers=headers)
            response = urllib.request.urlopen(request)
            soup = BeautifulSoup(response)
            json_text=soup.text
            data=json.loads(json_text)
            result=data['results']
            for item in result:
                card_ids.append(item['card_id'])
            print('page:{}'.format(page))

            page+=1
        except:
            print('page:{}'.format(page))
            print('done')
            break
    ff=open('card_ids.txt','w')
    for id in card_ids:
        ff.write(str(id)+'\n')
    ff.close()

def get_detail_info(headers):
    card_ids=[id.strip() for id in open('card_ids.txt')]
    import pandas as pd
    example={'id': 237086, 'user_id': 1034939,
                    'avatar_url': 'http://image.daqinjia.cn/adminplus/19574483-f6cc-43f9-b67f-25e3d3183ff9.png',
                    'gender': '女', 'birthday': '1991年2月', 'height': '161', 'residence': '河南省-商丘市', 'education': '本科',
                    'occupation': '市场部主管', 'income': '5千到1万', 'car': '无车', 'marriage': '未婚', 'introduction': '暂无',
                    'spouse': '暂无', 'house': '未购房', 'images': [], 'all_per': 0.95, 'mobile_phone': '15515937697',
                    'residence_new': '河南省-郑州市'}
    cols=[col for col in example]
    # res=pd.DataFrame(columns=cols)
    res={key:[] for key in example}
    for id in card_ids:
        personal_url = 'https://wxapp.daqinjia.cn/wx/api/qcard/v1/card/cardinfo/?card_id={}'.format(id)
        request = urllib.request.Request(url=personal_url, headers=headers)
        response = urllib.request.urlopen(request)
        soup = BeautifulSoup(response)
        json_text = soup.text
        if len(json_text) >0:
            data = json.loads(json_text)
            result = data['card_info']
            for key in result:
                res[key].append(result[key])
        else:
            print("can't find {}".format(id))
    res=pd.DataFrame(res)
    res.to_csv('card_infos.tsv',index=False,sep='\t')


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

    temps = soup.find_all('li', attrs={'class':"gl-item"})
    books=[]

    for tag in temps:
        name=tag.find('div', class_='p-name').get_text().strip()
        price = tag.find('div', class_='p-price').get_text().strip()
        img=tag.find('div', class_='p-img').a.img['source-data-lazy-img']
        print(0)


        pass


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
