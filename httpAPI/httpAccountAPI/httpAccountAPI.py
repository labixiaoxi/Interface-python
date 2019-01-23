# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/17 11:23
from public.publicLogs import PublicLogs
from public.publicMd5 import PublicMd5
from public.publicYaml import PublicGetYaml
from sql.sqlMessage import SqlMessage
from httpAPI.httpMethod import HttpMethod
from httpAPI.httpUserAPI.httpUserAPI import HttpUserAPI
log = PublicLogs()

class HttpAccountAPI:
    def __init__(self,yamlAccountPath,yamlUserPath,mobile,password):
        self.uri=PublicGetYaml(yamlAccountPath).get_Yaml()['Account']['uri']
        self.message = SqlMessage()
        self.md5=PublicMd5()
        self.userId = (HttpUserAPI(yamlUserPath).httpJhjLoginJson(mobile,password))['data']['uid']
        self.token = (HttpUserAPI(yamlUserPath).httpJhjLoginJson(mobile,password))['data']['token']
        self.role = (HttpUserAPI(yamlUserPath).httpJhjLoginJson(mobile,password))['data']['userType']
        self.page = 1
        self.pageSize = 100

    def httpUserHome(self):
        """
        我的账户
        :return:
        """
        role = 2
        self.url="hjlc-api/user/home?userId=%s&token=%s&role=%s"%(self.userId,self.token,role)
        return HttpMethod(self.uri,self.url).http_get()

    def httpUserCheckBindBank(self):
        """
        我的银行卡
        :return:
        """
        self.url="hjlc-api/user/checkBindBank?userId=%s&token=%s&role=%s"%(self.userId,self.token,self.role)
        return HttpMethod(self.uri,self.url).http_get()

    def httpUserAccountStat(self):
        """
        账户余额
        :return:
        """
        self.url="hjlc-api/user/accountStat?userId=%s&token=%s&role=%s"%(self.userId,self.token,self.role)
        return HttpMethod(self.uri,self.url).http_get()

    def httpTradeRecordLists(self,category):
        """
        交易记录
        :param category: 全部:为空, 充值:2, 提现:1 ,出借:3, 已赎回:5, 奖励:4
        :return:
        """
        self.url = "hjlc-api/trade/recordLists?userId=%s&role=%s&page=%s&pageSize=%s&category=%s"%(self.userId,self.role,self.page,self.pageSize,category)
        return HttpMethod(self.uri,self.url).http_get()

    def httpUserBank(self):
        """
        我的银行卡
        :return:
        """
        self.url = "hjlc-api/user/bank?userId=%s&role=%s"%(self.userId,self.role)
        return HttpMethod(self.uri,self.url).http_get()

    def httpUserAccount(self):
        """
        提现
        :return:
        """
        self.url = "hjlc-api/user/account?userId=%s&token=%s&role=%s"%(self.userId,self.token,self.role)
        return HttpMethod(self.uri,self.url).http_get()

    def httpUserAssetStat(self):
        """
        持有金额,累计金额,预计金额
        :return:
        """
        self.url="/hjlc-api/user/assetStat?userId=%s&token=%s"%(self.userId,self.token)
        return HttpMethod(self.uri,self.url).http_get()

    def httpInvestRecordLists(self,type):
        """
        智慧投订单列表
        :param type: 持有中:1 已赎回:2 赎回中:3
        :return:
        """
        self.url="hjlc-api/invest/recordLists?userId=%s&page=%s&pageSize=%s&type=%s"%(self.userId,self.page,self.pageSize,type)
        return HttpMethod(self.uri,self.url).http_get()

    def httpOrderDirectHome(self,currentStatus):
        """
        我的直投:持有资产,累计收益,待收收益,持有中订单
        :param currentStatus: 持有中:6 已还款10,14
        :return:
        """
        self.url="hjlc-api/order/direct/home?userId=%s&page=%s&pageSize=%s&currentStatus=%s"%(self.userId,self.page,self.pageSize,currentStatus)
        return HttpMethod(self.uri,self.url).http_get()

    def httpBankAvbList(self):
        """
        更换银行卡
        :return:
        """
        self.url="hjlc-api/bank/avb/list?"
        return HttpMethod(self.uri,self.url).http_get()

    def httpPartnerRewardAccount(self):
        """
        合伙人账户
        :return:
        """
        self.url="hjlc-api/partner/reward/account?userId=%s"%(self.userId)
        return HttpMethod(self.uri,self.url).http_get()

    def httpPartnerSettledList(self):
        """
        奖励明细
        :return:
        """
        self.url="hjlc-api/partner/settled/list?userId=%s"%(self.userId)
        return HttpMethod(self.uri,self.url).http_get()

    def httpPartnerTeamCount(self):
        """
        我的团队
        :return:
        """
        self.url="hjlc-api/partner/teamCount?userId=%s"%self.userId
        return HttpMethod(self.uri,self.url).http_get()

    def httpPartnerTeamList(self,type):
        """
        推荐关系
        :param type:直接推荐:1 间接推荐:2
        :return:
        """
        self.url="hjlc-api/partner/teamList?userId=%s&page=%s&pageSize=%s&type=%s"%(self.userId,self.page,self.pageSize,type)
        return HttpMethod(self.uri,self.url).http_get()

    def http(self,status):
        """
        我的卡包
        :param status:未使用:new 已使用:Used  已过期:Expire
        :return:
        """
        self.url="http://123.56.13.177:9090/hjlc-api/coupon/my/list?currentPage=%s&pageSize=%s&status=%s&userId=%s"%(self.page,self.pageSize,status,self.userId)
        return HttpMethod(self.uri,self.url).http_get()








