# -*- coding: utf-8 -*-
# @Time : 2020/7/30 4:47 下午
# @Author : shiro
# @Software: PyCharm
import requests,random,time

# URL = {
#
#     # https://lab.isaaclin.cn/nCoV/api/area?latest=1&province=日本
#     '全国疫情': 'https://lab.isaaclin.cn/nCoV/api/overall'
# }
# data = requests.get(URL['全国疫情']).json()
# print(data['results'][0]['confirmedCount'])


def City():
    with open('util/City.txt') as file:
        return file.read()


def getData(city):
    CityData = requests.get(f'https://lab.isaaclin.cn/nCoV/api/area?latest=1&province={city}').json()['results'][0]
    # print(CityData)
    return f'''地区(国家):{CityData['provinceName']}
现存确诊人数{CityData['currentConfirmedCount']}人
累计确诊人数{CityData['confirmedCount']}人
疑似感染人数{CityData['suspectedCount']}人
治愈人数{CityData['curedCount']}人
死亡人数{CityData['deadCount']}人
数据来源于丁香园(https://www.dxy.cn)
最后统计于{time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(CityData["updateTime"]/1000))}'''


def getNews():
    try:
        fakeNews = \
        requests.get(f'https://lab.isaaclin.cn/nCoV/api/rumors?page={random.randrange(1,2)}&num={random.randrange(100)}').json()['results'][0]
        return f'''标题:{fakeNews['title']}
概述:{fakeNews['mainSummary']}
内容:{fakeNews['body']}'''
    except:
        print('get news fail,retry')
        getNews()




# print(getNews())
# print('重庆市' in City())
# print(getData('中国'))
