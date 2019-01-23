# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/17 11:09
from httpAPI.httpProductAPI.httpProductAPI import HttpProductAPI
from public.publicYaml import PublicGetYaml
from sql.sqlProduct import SqlProduct
import unittest,HTMLTestRunner
class TestUserAPI(unittest.TestCase):
    def setUp(self):
        yamlProductPath = "yamlData/yamlProduct.yaml"
        self.product = HttpProductAPI(yamlProductPath)
        self.data = PublicGetYaml(yamlProductPath).get_Yaml()['product']
        self.sql = SqlProduct()



    def testHttpProductGreenHand(self):
        """活动推荐"""
        sql = "select * from product where category=1 and sell_end_time>=(SELECT DATE_FORMAT(NOW(),'%Y-%m-%d %H:%i:%S')) and current_status=2 and is_green_hand='Y';"
        result_sql = self.sql.product(sql)
        response = self.product.httpProductGreenHand()
        #判断sql返回结果
        if result_sql == 0:
            total = 0
            self.assertEqual(total,response['data']['recommendProducts'],msg=u"response异常,请确认")
        else:
            # 产品名称
            sql_productName = result_sql[0][3]
            # 产品加息
            sql_marketingRate = result_sql[0][38]
            self.assertEqual(str(sql_productName),str(response['data']['greenHandProducts'][0]['productName']),msg=u"response异常,请确认")
            self.assertEqual(str(sql_marketingRate),str(response['data']['greenHandProducts'][0]['marketingRate']),msg=u"response异常,请确认")
        self.assertEqual(200,response['code'],msg=u"response返回状态异常,请确认")

    def testHttpIndexProductList001(self):
        """智慧投列表"""
        sql = "select * from product where category=1 and sell_end_time>=(SELECT DATE_FORMAT(NOW(),'%Y-%m-%d %H:%i:%S')) and current_status=2 and is_marketing='N';"
        result_sql = self.sql.product(sql)
        category = 1
        response = self.product.httpIndexProductList(category)
        if result_sql == 0:
            total = 0
            self.assertEqual(total,response['data']['total'],msg=u"response异常,请确认")
        else:
            sql_total = len(result_sql)
            self.assertEqual(str(sql_total),str(response['data']['total']),msg=u"response异常,请确认")
        self.assertEqual(200,response['code'],msg=u"response返回状态异常,请确认")


    def testHttpIndexProductList002(self):
        """直投列表"""
        sql = "select * from product where category=2 and sell_end_time>=(SELECT DATE_FORMAT(NOW(),'%Y-%m-%d %H:%i:%S')) and (current_status=6 or current_status=7 or current_status=8)"
        result_sql = self.sql.product(sql)
        category = 2
        response = self.product.httpIndexProductList(category)
        if result_sql == 0:
            total = 0
            self.assertEqual(total,response['data']['total'],msg=u"response异常,请确认")
        else:
            sql_total = len(result_sql)
            self.assertEqual(sql_total,response['data']['total'],msg=u"response异常,请确认")
        self.assertEqual(200,response['code'],msg=u"response返回状态异常,请确认")

    def testHttpProductDetail(self):
        """智慧投出借详情"""
        sql = "select * from product where sell_end_time>=(SELECT DATE_FORMAT(NOW(),'%Y-%m-%d %H:%i:%S')) and current_status=2;"
        result_sql = self.sql.product(sql)
        for i in range(len(result_sql)):
            result_id = result_sql[i][0]
            response= self.product.httpProductDetail(result_id)
            result_name = result_sql[i][3]
            self.assertEqual(str(result_name),str(response['data']['name']),msg=u"response异常,请确认,产品id:%s"%result_id)
            self.assertEqual(200,response['code'],msg=u"response返回状态异常,请确认")



    def testHttpProductDirectDetail(self):
        """直投出借详情"""
        # sql = "select * from product where sell_end_time>=(SELECT DATE_FORMAT(NOW(),'%Y-%m-%d %H:%i:%S')) and category=2;"
        # result_sql = self.sql.product(sql)
        # for i in range(len(result_sql)):
        #     result_id = result_sql[i][0]
        #     response= self.product.httpProductDirectDetail(result_id)
        #     result_name = result_sql[i][3]
        #     result_baseRate =  result_sql[i][44]
        #     result_interestRate =  result_sql[i][45]
        #     self.assertEqual(str(result_name),str(response['data']['name']),msg=u"response异常,请确认,产品id:%s"%result_id)
        #     self.assertEqual(float(result_baseRate),float(response['data']['interestRate']),msg=u"response异常,请确认,产品id:%s"%result_id)
        #     self.assertEqual(float(result_interestRate),float(response['data']['increasedInterestRate']),msg=u"response异常,请确认,产品id:%s"%result_id)
        #     self.assertEqual(200,response['code'],msg=u"response返回状态异常,请确认")


    def testHttpProductDetailWithAccount(self):
        """授权出借"""
        # 需要考虑产品是否有可购买金额
        # sql = "select * from product where sell_end_time>=(SELECT DATE_FORMAT(NOW(),'%Y-%m-%d %H:%i:%S')) and (current_status=6 or current_status=2);"
        # result_sql = self.sql.product(sql)
        # for i in range(len(result_sql)):
        #     result_id = result_sql[i][0]
        #     self.userId = self.data['userId']
        #     response = self.product.httpProductDetailWithAccount(result_id,self.userId)
        #     print response
        #     print self.userId
        #     print result_id
        #     self.assertEqual(200,response['code'],msg=u"response返回状态异常,请确认,产品id:%s"%result_id)

    def testHttpProductInvestList(self):
        """投资记录"""
        sql = "select * from product where sell_end_time>=(SELECT DATE_FORMAT(NOW(),'%Y-%m-%d %H:%i:%S')) and (current_status=6 or current_status=2);"
        result_sql = self.sql.product(sql)
        for i in range(len(result_sql)):
            result_id = result_sql[i][0]
            response = self.product.httpProductInvestList(result_id)
            self.assertEqual(200,response['code'],msg=u"response返回状态异常,请确认")


if __name__ == '__main__':
    unittest.main()