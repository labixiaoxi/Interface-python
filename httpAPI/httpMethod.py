# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/17 10:13
import requests
from public.publicLogs import PublicLogs
log = PublicLogs()
class HttpMethod(object):
    def __init__(self,uri,url,data=None):
        self.uri=uri
        self.url=url
        self.data=data

    def http_post(self):
        res = requests.post(url=self.uri+self.url,data=self.data)
        if res.status_code == 200:
            log.info(u"request:%s, data:%s, response:%s"%(self.uri+self.url,self.data,res.text))
        else:
            log.info(u"status异常")
        return res.json()


    def http_get(self):
        res = requests.get(url=self.uri+self.url)
        if res.status_code == 200:
            log.info(u"request:%s"%(self.uri+self.url))
            log.info(u"response:%s"%(res.text))
            return res.json()
        else:
            log.info(u"status异常")
        return res.json()