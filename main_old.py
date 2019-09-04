# -*- coding: utf-8 -*-
import requests
import json
import random
from requests.cookies import RequestsCookieJar
import pprint
import time

headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'}
#cookies = {}
##在这里添加cookies
#cookies_str = 'pgv_pvi=6699446272; pgv_si=s1430532096; mail="2|1:0|10:1563160766|4:mail|44:cG9lcW5jaWhAbWFpbC5iY2N0by5tZXwxNTYzMTYwNzY2|b799ecb08468b13d581b8b6db9a67c49214352cc4ee6115b91fd659ab3c2c408"; time="2|1:0|10:1563160766|4:time|16:MTU2MzE2MDc2Ng==|190abcb58d35b0de71b59c4d2159a27680b1ecde69216fae2ea4c566dbae7646"'
#cookies_list = cookies_str.split(';')
#for tmp in cookies_list:
#    name = tmp.split('=',1)[0]
#    value = tmp.split('=',1)[1]
#    cookies[name] = value
#pprint.pprint(cookies)
#print(time.time())
#response = requests.post('http://mail.bccto.me/applymail', headers=headers)
#cookies = response.cookies.get_dict()
def apply():
    mail_front = []
    i = 0
    
    mima = []
    for i in range(8):
        mima.append(random.choice('abcdefghijklmnopqrstuvwxyz123456789'))
    mima = "".join(mima)

    apply_url = 'http://mail.bccto.me/applymail'
    for i in range(8):
        mail_front.append(random.choice('abcdefghijklmnopqrstuvwxyz123456789'))
    mail_front = "".join(mail_front)
    mail = mail_front + '@899079.com'
    apply_data = {'mail':mail}
    
    r_apply = requests.post(apply_url,headers=headers, data=apply_data, cookies=cookies)
    print(r_apply)
    assert json.loads(r_apply.content)['success']=='true'
    return mail,mima
def ifget_mail(mail):
    get_url = 'http://mail.bccto.me/getmail'
    get_data = {'mail':mail}
    r_get = requests.post(get_url, headers=headers, data=get_data, cookies=cookies)
    return json.loads(r_get.content)['mail']
def find_mail(mail,get_mail_url_last):
    url = 'http://mail.bccto.me/win/'+mail.split('@')[0]+'(a)899079-_-com/' + get_mail_url_last
    r_find = requests.get(url, headers=headers, cookies=cookies)
    www = r_find.content.decode().split('号')[1].split('官')[0].split('>')[3].split('<')[0]
    r_apply = requests.get(www, headers=headers, cookies=cookies)
    return www
def register(mail,mima):
    data = {
            'email':mail,
            'email2':mail,
            'password':mima,
            'password2':mima
            }
    time_ = time.time()
    url = 'https://www.chromehelper.net/server/account/signup?gtoken=5c35583e6994af913318c5350ea8a72b&version=1.4.3&proxy_pac_key=7e99c7debee0aa8a586862568830f556&api_url=https%3A%2F%2Fwww.chromehelper.net&lang=zh-CN&client_id=nonmafimegllfoonjgplbabhmgfanaka&time=' + str(time_)
    r = requests.post(url, headers=headers, data=data, cookies=cookies)
def login(mail, mima):
    time_ = time.time()   
    url = 'https://www.speedstunnel.com/server/account/login?gtoken=5c35583e6994af913318c5350ea8a72b&version=1.4.3&proxy_pac_key=9fe764f0b5f3a45dccf8712332b8eb5d&api_url=https%3A%2F%2Fwww.speedstunnel.com&lang=zh-CN&client_id=nonmafimegllfoonjgplbabhmgfanaka&time=' + str(time_)
    data = {
            'email':mail,
            'password':mima
            }
    r = requests.post(url, headers=headers, data=data, cookies=cookies)
if __name__ == '__main__':
    mail,mima = apply()
    register(mail,mima)
    if_get_mail = ifget_mail(mail)
    while(len(if_get_mail)==0):
        if_get_mail = ifget_mail(mail)
    find_mail(mail, if_get_mail[0][-2])    
#    print(mail+'\n'+mima)
    login(mail, mima)
   
    