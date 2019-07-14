# -*- coding: utf-8 -*-
import requests
import json
import random
from requests.cookies import RequestsCookieJar
import pprint


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
cookies = {}
cookies_str = 'pgv_pvi=9906049024; UM_distinctid=16ba10ac40126d-08a948ed81d7ed-3c604504-1fa400-16ba10ac40215f; pgv_si=s961515520; CNZZDATA3645431=cnzz_eid%3D109612578-1561769735-null%26ntime%3D1562976090; lang="2|1:0|10:1562980538|4:lang|8:emhfQ04=|409ad47e37f2606dc088938a1963fd355c9cb50cd890cfc6812e773a6745b13b"; mail="2|1:0|10:1562980560|4:mail|40:cGEwM3JiYXZAODk5MDc5LmNvbXwxNTYyOTgwNTYw|b56035f6069e14a832e155a6f83b21b201bbd0ba6c6031082ee9a309e5c031a6"; time="2|1:0|10:1562980560|4:time|16:MTU2Mjk4MDU2MA==|bc764d90c6dfdcd93d2e2ddf45adfecf8a6b3f13886b502272e7d45809a8d0f4"'
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
#    print(r_get.content)
    return json.loads(r_get.content)['mail']
def find_mail(get_mail_url_last):
    url = 'http://mail.bccto.me/win/s94h0nbe(a)899079-_-com/' + get_mail_url_last
    r_find = requests.get(url, headers=headers, cookies=cookies)
    www = r_find.content.decode().split('号')[1].split('官')[0].split('>')[3].split('<')[0]
    r_apply = requests.get(www, headers=headers, cookies=cookies)
#    print(r_apply)
    return www
#def 
if __name__ == '__main__':
    mail,mima = apply()
    print(mail,mima)
    if_get_mail = ifget_mail(mail)
    while(len(if_get_mail)==0):
        if_get_mail = ifget_mail(mail)
    find_mail(if_get_mail[0][-2])

#    find_mail('KJBE90Tu3oq3u9fRkEXGVG.eml')
    