# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:39:11 2019

@author: dell
"""

import requests
#
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#cookies = {}
#cookies_str = 'pgv_pvi=9906049024; UM_distinctid=16ba10ac40126d-08a948ed81d7ed-3c604504-1fa400-16ba10ac40215f; pgv_si=s961515520; CNZZDATA3645431=cnzz_eid%3D109612578-1561769735-null%26ntime%3D1562976090; lang="2|1:0|10:1562980538|4:lang|8:emhfQ04=|409ad47e37f2606dc088938a1963fd355c9cb50cd890cfc6812e773a6745b13b"; mail="2|1:0|10:1562980560|4:mail|40:cGEwM3JiYXZAODk5MDc5LmNvbXwxNTYyOTgwNTYw|b56035f6069e14a832e155a6f83b21b201bbd0ba6c6031082ee9a309e5c031a6"; time="2|1:0|10:1562980560|4:time|16:MTU2Mjk4MDU2MA==|bc764d90c6dfdcd93d2e2ddf45adfecf8a6b3f13886b502272e7d45809a8d0f4"'
#cookies_list = cookies_str.split(';')
#for tmp in cookies_list:
#    name = tmp.split('=',1)[0]
#    value = tmp.split('=',1)[1]
#    cookies[name] = value
#r = requests.get('http://mail.bccto.me/win/s94h0nbe(a)899079-_-com/b2kEtHWIwc85qFrBJGv720.eml',headers=headers,cookies=cookies)
#print(r)
#print(r.content.decode())
##print(r.content.decode().split('号')[1].split('官')[0].split('>')[3].split('<')[0])
##print(r.content.decode().split('号')[1].split('官')[0].split('>')[3].split('<')[0])
#http://mail.bccto.me/win/h0ew3rys(a)899079-_-com/b2kEtHWIwc85qFrBJGv720.eml
#http://mail.bccto.me/win/s94h0nbe(a)899079-_-com/b2kEtHWIwc85qFrBJGv720.eml
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')