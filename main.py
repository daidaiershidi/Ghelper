# -*- coding: utf-8 -*-
import requests
import json
import random
from requests.cookies import RequestsCookieJar
import pprint
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
cookies = {}
#在这里添加cookies
cookies_str = ''
cookies_list = cookies_str.split(';')
for tmp in cookies_list:
    name = tmp.split('=',1)[0]
    value = tmp.split('=',1)[1]
    cookies[name] = value
###################
#获取十分钟邮箱账号##
##################
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
    #print(data)
    
    r_apply = requests.post(apply_url,headers=headers, data=apply_data, cookies=cookies)
    assert json.loads(r_apply.content)['success']=='true'
    return mail,mima
######################
#是否获取邮箱的邮件内容##
#####################
def ifget_mail(mail):
    get_url = 'http://mail.bccto.me/getmail'
    get_data = {'mail':mail}
    r_get = requests.post(get_url, headers=headers, data=get_data, cookies=cookies)
#    print(r_get.content.decode())
    return json.loads(r_get.content)['mail']
def find_mail(mail,get_mail_url_last):
    url = 'http://mail.bccto.me/win/'+mail.split('@')[0]+'(a)899079-_-com/' + get_mail_url_last
#    print(url)
    r_find = requests.get(url, headers=headers, cookies=cookies)
    www = r_find.content.decode().split('号')[1].split('官')[0].split('>')[3].split('<')[0]
    r_apply = requests.get(www, headers=headers, cookies=cookies)
#    print(r_apply)
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
#    print(r.content.decode())
def login(mail, mima):
    time_ = time.time()   
    url = 'https://www.speedstunnel.com/server/account/login?gtoken=5c35583e6994af913318c5350ea8a72b&version=1.4.3&proxy_pac_key=9fe764f0b5f3a45dccf8712332b8eb5d&api_url=https%3A%2F%2Fwww.speedstunnel.com&lang=zh-CN&client_id=nonmafimegllfoonjgplbabhmgfanaka&time=' + str(time_)
    data = {
            'email':mail,
            'password':mima
            }
    r = requests.post(url, headers=headers, data=data, cookies=cookies)
    print(r)
if __name__ == '__main__':
    mail,mima = apply()
    register(mail,mima)
    if_get_mail = ifget_mail(mail)
    while(len(if_get_mail)==0):
        if_get_mail = ifget_mail(mail)
    find_mail(mail, if_get_mail[0][-2])    
    print(mail+'\n'+mima)
    login(mail, mima)
#    register('h0ew3rys@899079.com','11112222')
#    
#    if_get_mail = ifget_mail('h0ew3rys@899079.com')
#    while(len(if_get_mail)==0):
#        if_get_mail = ifget_mail('h0ew3rys@899079.com')
#    find_mail(if_get_mail[0][-2])
#    i=0
#    while(i<100):
#        register('ollxdz6q@899079.com','11111123')
#    
    