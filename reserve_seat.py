#!/usr/bin/python
# -*- coding: UTF-8 -*-
#@revenge_time.py
#@origin:wheee && RenjiaLu
#@recoder:Jetdky
#@time:2018-10-03



import requests
import time
from datetime import date, datetime
#自抓取
WECHATSESS_ID = "2a43218267d8e4611f155add923f8787"
HM_LVT = "1538557699"

headers = {
'Host': 'wechat.v2.traceint.com',
'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0.2; vivo Y35A Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/WIFI Language/zh_CN Process/tools',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/wxpic,image/sharpp,image/apng,image/tpg,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,en-US;q=0.8'
}

cookies = dict(
    FROM_TYPE="weixin",
    Hm_lvt_7ecd21a13263a714793f376c18038a87 = HM_LVT,
    Hm_lpvt_7ecd21a13263a714793f376c18038a87 = str(int(time.time())),
    wechatSESS_ID = WECHATSESS_ID
)

class Jetdky:
    R2_SEAT={
        '192':'28,13',
        '193':'28,14',
        '183':'28,4'
    }
    R3_SEAT={
        '1':'6,6',
        '2':'6,7',
        '3':'6,8',
        '4':'6,9',
        '5':'10,9',
        '6':'10,8',
        '7':'10,7',
        '8':'10,6',
        '9':'14,6',
        '10':'14,7',
        '11':'14,8',
        '12':'14,9',
        '13':'18,9',
        '14':'18,8',
        '15':'18,7',
        '16':'18,6',
        '17':'22,6',
        '18':'22,7',
        '19':'22,8',
        '20':'22,9',
        '21':'6,13',
        '22':'6,14',
        '23':'6,15',
        '24':'6,16',
        '25':'10,16',
        '26':'10,15',
        '27':'10,14',
        '28':'10,13',
        '29':'14,13',
        '30':'14,14',
        '31':'14,15',
        '32':'14,16',
        '33':'18,16',
        '34':'18,15',
        '35':'18,14',
        '36':'18,13',
        '37':'22,13',
        '38':'22,14',
        '39':'22,15',
        '40':'22,16',
        '41':'6,20',
        '42':'6,21',
        '43':'6,22',
        '44':'10,22',
        '45':'10,21',
        '46':'10,20',
        '47':'14,20',
        '48':'14,21',
        '49':'14,22',
        '50':'18,22',
        '51':'18,21',
        '52':'18,20',
        '53':'22,20',
        '54':'22,21',
        '55':'22,22',
        '56':'26,22',
        '57':'26,21',
        '58':'26,20',
        '59':'6,26',
        '60':'6,27',
        '61':'6,28',
        '62':'6,29',
        '63':'10,29',
        '64':'10,28',
        '65':'10,27',
        '66':'14,27',
        '67':'14,28',
        '68':'14,29',
        '69':'18,29',
        '70':'18,28',
        '71':'18,27',
        '72':'22,27',
        '73':'22,28',
        '74':'22,29',
        '75':'26,29',
        '76':'26,28',
        '77':'26,27',
        '78':'6,33',
        '79':'6,34',
        '80':'6,35',
        '81':'6,36',
        '82':'10,36',
        '83':'10,35',
        '84':'10,34',
        '85':'14,34',
        '86':'14,35',
        '87':'14,36',
        '88':'18,36',
        '89':'18,35',
        '90':'18,34',
        '91':'22,34',
        '92':'22,35',
        '93':'22,36',
        '94':'26,35',
        '95':'26,34',
        '96':'10,40',
        '97':'10,41',
        '98':'10,42',
        '99':'10,43',
        '100':'14,43',
        '101':'14,42',
        '102':'14,41',
        '103':'14,40',
        '104':'18,40',
        '105':'18,41',
        '106':'18,42',
        '107':'18,43',
        '108':'22,43',
        '109':'22,42',
        '110':'22,41',
        '111':'22,40'
    }
    ROOM={
        "ROOM_2":"1034",
        "ROOM_3":"1032"
    }
    def __init__(self):
        pass


def login_in_and_reserve_seat(headers, cookies, ROOMID, SEATID):
    student = Jetdky()
    roomval = student.ROOM["ROOM_2" if ROOMID == "2" else "ROOM_3" ]
    seatval = (student.R2_SEAT if ROOMID == "2" else student.R3_SEAT)[SEATID]
    LOGIN_IN_URL = "https://wechat.v2.traceint.com/index.php/reserve/index.html?f=wechat"
    RESERVE_URL = "http://wechat.v2.traceint.com/index.php/reserve/get/libid=%s&key=%s&yzm=" % (roomval,seatval)
    s = requests.session()
    
    try:
        s.get(LOGIN_IN_URL, timeout=1, headers=headers, cookies=cookies, verify = False)
    except Exception as e:
        print("登录“来选座”出错,错误原因：%s\n" % (e))
    else:
        print("登录“来选座”成功\n")
    try:
        response = s.get(RESERVE_URL, timeout=1, headers=headers, cookies=cookies, verify = False)
    except Exception as e:
        print("座位预定出错,错误原因 %s\n" % (e))
    else:
        if(response.text.find("预定成功") > 0):
            print("座位预定成功！成功预定第%s自习室，第%s号座位 - 服务器返回状态码为%s" % (ROOMID,SEATID,response.status_code),"\n")
            return True
        elif(response.text.find("被人预定") > 0):
            print("该座位已经被人预订了\n")
            return False
def login_in_and_reserve_seat_tomorrow(headers, cookies, ROOMID, SEATID):
    student = Jetdky()
    roomval = student.ROOM["ROOM_2" if ROOMID == "2" else "ROOM_3" ]
    seatval = (student.R2_SEAT if ROOMID == "2" else student.R3_SEAT)[SEATID]
    LOGIN_IN_URL = "https://wechat.v2.traceint.com/index.php/reserve/index.html?f=wechat"
    RESERVE_TOMORROW_URL = "http://wechat.v2.traceint.com/index.php/prereserve/save/libid=%s&key=%s&yzm=" % (roomval,seatval)
    s = requests.session()
    
    try:
        s.get(LOGIN_IN_URL, timeout=1, headers=headers, cookies=cookies, verify = False)
    except Exception as e:
        print("登录“来选座”出错,错误原因：%s\n" % (e))
    else:
        print("登录“来选座”成功\n")

    try:
        response = s.get(RESERVE_TOMORROW_URL, timeout=1, headers=headers, cookies=cookies, verify = False)
    except Exception as e:
        print("明日预定出错,错误原因 %s\n" % (e))
    else:
        if(response.text.find("请准时到") > 0):
            print("座位预定成功！成功预定第%s自习室，第%s号座位 - 服务器返回状态码为%s" % (ROOMID,SEATID,response.status_code),"\n")
            return True
        elif(response.text.find("被人预定") > 0):
            print("该座位已经被人预订了\n")
            return False
if __name__ == '__main__':
    judge = input("预约输入1， 明日预约输入2\n")
    if("1" == judge):
        login_in_and_reserve_seat(headers, cookies, "3", "68")
    elif("2" == judge):
        login_in_and_reserve_seat_tomorrow(headers, cookies, "3", "68")