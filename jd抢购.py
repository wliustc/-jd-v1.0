# -*- coding: UTF-8 -*-
import requests
import re
import datetime
import time
id=raw_input('please show your buything id:')
target_time=raw_input('please input buy time:example input:10:00\n')
mycookie=raw_input('please input your cookie:')
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
'Accept':'*/*',
'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding':'gzip, deflate',
'Referer':'https://item.jd.com/'+id+'.html',
'Connection':'close',
'Cookie':mycookie
}
n=2
def get_url1(headers):
  url1='https://passport.jd.com/loginservice.aspx?callback=jQuery9109827&method=Login&_=1551614045664'
  requests.get(url=url1,headers=headers)
  print('url1:ok')
def get_url2(headers,id):
  url2='https://easybuy.jd.com/skuDetail/newSubmitEasybuyOrder.action?callback=easybuysubmit&skuId=%s&num=1&gids=&ybIds=&did=&useOtherAddr=false&_=1551614116353'%id
  res=requests.get(url=url2,headers=headers)
  print('url2:ok')
  return res
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')             
nowTime=nowTime[11:]                                                       #截取时间形如22:40:11
nowTime_s=(int(nowTime[0:2])*60+int(nowTime[3:5]))*60+int(nowTime[6:8])    #将当前时间换算成秒
target_time_s=(int(target_time[0:2])*60+int(target_time[3:5]))*60          #将抢购的时间转换成秒
sleep_time=target_time_s-nowTime_s
print(sleep_time)
time.sleep(sleep_time-2)                                                        #提前三秒开始运行脚本 
while True:
  get_url1(headers)
  res=get_url2(headers,id)
  str=res.text  #res.text形如 str='easybuysubmit({"message":null,"success":true,"jumpUrl":"//trade.jd.com/shopping/order/getOrderInfo.action?rid=1551620761368"});'
  pattern=re.compile(r'\"success\":true')
  if (pattern.search(str)):
    pattern=re.compile(r'//.+')
    url=pattern.findall(str)[0].rstrip(';)}"')                             #正则抽取jumpurl的内容 
    location_url='https:'+url                                              #location跳转地址为订单结算页面
    print 'Success!please copy list url to your browser!'
    print '%s'%location_url
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    break
  else:
    print '%d'%n
    n=n+1
