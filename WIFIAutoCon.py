import requests
import time
import datetime
import os
import sys
from threading import Thread
from win10toast import ToastNotifier

def loginCampusNetwork():
    #登录地址
    post_addr="http://172.16.30.45//drcom/login"

    #构造头部信息
    post_header={
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection':'keep-alive',
    'DNT': '1',
    'Host': '172.16.30.45',
    'Referer':'http://172.16.30.45/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'X-Requested-With':'XMLHttpRequeste'
    }

    of = open(os.path.dirname(os.path.realpath(sys.executable))+"\idpassword.txt","r")
    lines = of.read().splitlines()  # 读取所有行
    id = lines[0]  # 取第一行
    password = lines[1]  # 取第二行

    t=time.time()*1000

    #构造登录数据
    post_data={'callback':('dr'+(str(round(t)))),
           'DDDDD':(''+id),
           'upass':''+password,
           '0MKKey':'123456',
           'R1':'0',
           'R3':'1',
           'R6':'0',
           'para':'00',
           'v6ip':'',
           '_':(str(round(t)))
          }   
    #发送post请求登录网页
    response=requests.post(post_addr,data=post_data,headers=post_header)

    result = "失败"

    if "user-scalable=yes" in response.text:
        result = "成功"

    toaster = ToastNotifier()

    toaster.show_toast("中大南方校园网登录",
                   "校园网认证"+result,
                   icon_path=os.path.dirname(os.path.realpath(sys.executable))+"\wifi.ico",
                   duration=10)

try:
    thread = Thread(target=loginCampusNetwork)
    thread.start()
except:
    toaster = ToastNotifier()

    toaster.show_toast("中大南方校园网登录",
                   "啊咧，程序出现错误了",
                   icon_path=os.path.dirname(os.path.realpath(sys.executable))+"\wifi.ico",
                   duration=10)