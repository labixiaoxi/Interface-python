# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/17 11:23
from public.publicLogs import PublicLogs
from public.publicMd5 import PublicMd5
from public.publicYaml import PublicGetYaml
from sql.sqlMessage import SqlMessage
from httpAPI.httpMethod import HttpMethod
log = PublicLogs()

class HttpProductAPI:
    def __init__(self,yamlProductPath):
        self.uri=PublicGetYaml(yamlProductPath).get_Yaml()['product']['uri']
        self.message = SqlMessage()
        self.md5=PublicMd5()

    def httpProductGreenHand(self):
        """
        活动推荐
        :return:
        """
        self.url="/hjlc-api/product/greenHand"
        return HttpMethod(self.uri,self.url).http_get()

    def httpIndexProductList(self,category):
        """
        智慧投和直投产品
        :param category:智慧投产品:1 直投产品:2
        :return:
        """
        pageSize=100
        category=category
        page=1
        self.url="/hjlc-api/index/product/list?pageSize=%s&category=%s&page=%s"%(pageSize,category,page)
        return HttpMethod(self.uri,self.url).http_get()

    def httpProductDetail(self,id):
        """
        智慧投出借详情
        :param id:产品id
        :return:
        """
        self.url="/hjlc-api/product/detail?id=%s"%id
        return HttpMethod(self.uri,self.url).http_get()

    def httpProductDirectDetail(self,id):
        """
        直投出借详情
        :param id:产品id
        :return:
        """
        self.url="/hjlc-api/product/direct/detail?id=%s"%id
        return HttpMethod(self.uri,self.url).http_get()

    def httpProductDetailWithAccount(self,id,userId):
        """
        授权出借
        :param id:产品id
        :param userId: 账号的userId
        :return:
        """
        self.url="/hjlc-api/product/detailWithAccount?id=%s&userId%s="%(id,userId)
        return HttpMethod(self.uri,self.url).http_get()

    def httpProductInvestList(self,id):
        """
        投资记录
        :param id: 产品id
        :return:
        """
        page = 1
        pageSize=100
        self.url="/hjlc-api/product/invest/list?id=%s&page=%s&pageSize=%s"%(id,page,pageSize)
        return HttpMethod(self.uri,self.url).http_get()

if __name__ == '__main__':
    http = HttpProductAPI( "../../yamlData/yamlProduct.yaml")
    # http.httpProductGreenHand()
    # http.httpIndexProductList(1)
    # http.httpIndexProductList(2)
    # http.httpProductDirectDetail(450)
    # http.httpProductDetailWithAccount()
    http.httpProductInvestList(9)










