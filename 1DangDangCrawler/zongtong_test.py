import urllib.request
from urllib import parse
from bs4 import BeautifulSoup
import json

def zhongtong(address):

    headers={'charset': 'utf-8',
           'x-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0aGlyZFBhcnR5U2lnbiI6IndlY2hhdE1pbmladG9IZWxwZXIiLCJzdWIiOiI1NTQyNTE2NiIsIm9wZW5JZCI6Im9KcFVJMFVvT1FxUWFZNkpzdW5PTUNEcTdIYzgiLCJpc3MiOiJXZWJVc2VyQ2VudGVyIiwibW9iaWxlIjoiMTMwMDY5MTI2MDEiLCJ1c2VySWQiOiI1NTQyNTE2NiIsImF1ZCI6IldlYlVzZXJDZW50ZXIiLCJ0aGlyZFBhcnR5VUlkIjoibzI3Vk50d0hiMk1aQXRKTWZMLTRKaVN0M200RSIsInRoaXJkUGFydHlBcHBDb2RlIjoid2VjaGF0TWluaVp0b0hlbHBlciIsImNsaWVudENvZGUiOiJ3ZWNoYXRNaW5pWnRvSGVscGVyIiwiZmF0IjoxNTc0ODI1NTI5LCJ0aGlyZFBhcnR5Q29kZSI6IndlY2hhdCIsInRoaXJkUGFydHlBcHBPcGVuSWQiOiJvSnBVSTBVb09RcVFhWTZKc3VuT01DRHE3SGM4IiwiZXhwIjoxNTc0ODQ3MTI5LCJpYXQiOjE1NzQ4MjU1MjksImp0aSI6ImIxNTFhN2MzODVkZTQ4ZjZhYjE3OTA2NDhmYTJhMjVmIn0.dySYSlHwNIFz68EBiX75RiigaF2GynLKF4oOkM1yf7rlxEN7YjBd7jCvr4RwdJS9ufjgxdbQgsjbfACVXG575JWKK5Gff9a4uj-H_tibZhHqclC4aM9N7xRVhXg-SuE_QDTzjvoP6ZapMnnqKh5hXoDPgaZgzn9VRbyINuHQlrPZPfcsBEN3jM3eXiW0bycLqJdW3tSsGecZXoD_wTKLuG1sv5BDF7N3wTpgqfDZv8Uza0I1PROBvd0b5KAN3rDu-vPTNa1-e3DSKH2k7VyPPQM_J3QjP6ZcP4Cvq8Hgvss86CsDKgsWFH6uREwXHnglpL6nvhuNIxqclOzROdSHqw',
          'referer': 'https://servicewechat.com/wx7ddec43d9d27276a/116/page-frame.html',
           'content-type': 'application/json',
           'x-clientcode': 'wechatMiniZtoHelper',
           'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 4X Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 MicroMessenger/7.0.8.1540(0x27000834) Process/appbrand2 NetType/WIFI Language/zh_CN ABI/arm64',
           'Host': 'hdgateway.zto.com'
           }
    url='https://hdgateway.zto.com/Word_AnalysisAddress'
    data="{'address':'"+address+"'}"
    data=bytes(data,encoding="utf-8")
    request = urllib.request.Request(url=url, headers=headers,data=data,method='POST')
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response)
    # print(soup.text)
    res = json.loads(soup.text)
    result=res["result"]["items"][0]
    del result['districtId']
    del result['cityId']
    del result['provinceId']
    del result['remark']
    print(result)

if __name__=="__main__":
    text='''桐梓 林东路一号 10栋 一单元
    15928188779'''
    text='''北京市海淀区万丰路十八号院2
     号楼1002  王小波 刘先生 于贝贝,18805123445'''
    # text='baby 17654325162 北京市海淀区致真大厦-a座'
    # text='收货。：1763330 1388。：河北 保定 安国 佳兴公寓 收货我家在收货哪西二旗'
    text='张学友电话是13467898765把这个蛋糕送到西北旺东路中关村 软件园博彦 科技大厦C座 '
    # text='''王小二 林东路一号 10栋 一单元
    text='北京 北京市 东城区 和平里 和平新城30号楼A座70A'
    text = '''收货人: 曹振天
    手机号码: 18519792042
    所在地区: 北京北京市海淀区马连洼街道刘德华
    详细地址: 圆明园西路9-6号美利达自行车店'''
    text = '张学友13467898765把这个蛋糕送到西北旺东路中关村 软件园博彦 科技大厦C座 '
    text='甘生,rise cake瑞思蛋糕(喜悦里店)（深圳市龙岗区龙岗街道喜悦里商业街2期14号商铺（南联地铁站B3出口直行50米尊宝披萨对面）），15643435656'
    # 15928188779'''
    text='麻烦你把东西寄到：朝阳区百子湾路后现代城3号楼C单元101号（小龙虾），李颖，17611656785'
    text='江左盟主 18767876567 北京大学西校门7号宿舍楼'
    text='天安门广场西单商业街6F丹尼斯 柜台 146-876-0987'
    text='麻烦你把东西寄到：朝阳区百子湾路后现代城3号楼C单元101号（小龙虾），李颖，17611656785'
    text='小低，北京市朝阳区延静里中街甲18号院2号非常虾，18310822840'
    text='17898754567 你大爷 龙域西二路融泽嘉园二号院一号楼2211'
    text='毛茗；IFS国际金融中心一号办公楼,一号办公楼；18090987663'
    text='琅西维也纳酒店四楼 刘德华 茶馆电话19968234163'
    text='淡定15989328009广东省深圳市福田区梅林街道上梅林梅华路祠堂村31栋1005'
    text='北京市朝阳区左家庄街道静安西街12号楼211室果果收15850721131'
    text='安卉15801152546工体北路21号屯三里21号永利国际三层爱奇艺青春中心'
    text='北京市朝阳门南大街18号 外企人力资源服务有限公司 洪飞 孙老师两篮 13521053166'
    text='浙江省杭州市余杭区乔司街道毛桃东街1号星达手机连锁15715709444李晓凯'
    text='17898754567 你大爷 龙域西二路融泽嘉园二号院一号楼2211'
    text='月坛南街泽湘苑大酒店vip003包厢，刘宝建，13717940035'
    zhongtong(text)