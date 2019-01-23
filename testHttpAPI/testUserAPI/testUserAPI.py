# # -*-coding:utf-8 -*-
# # __author__ = 'xiaoxi'
# # @time:2019/1/17 11:09
# from httpAPI.httpUserAPI.httpUserAPI import HttpUserAPI
# from public.publicYaml import PublicGetYaml
# from sql.sqlMember import SqlMember
# import unittest,HTMLTestRunner
# class TestUserAPI(unittest.TestCase):
#     def setUp(self):
#         yamlUserPath = "../../yamlData/yamlUser.yaml"
#         self.user = HttpUserAPI(yamlUserPath)
#         self.data = PublicGetYaml(yamlUserPath).get_Yaml()['user']
#
#     def testHttpJhjSmsRegisterJson001(self):
#         """注册发送验证码---未注册账号"""
#         mobile = self.data['mobile1']
#         mobile_list=[]
#         while len(mobile_list)!=1:
#             if SqlMember().member(mobile)==None:
#                 mobile_list.append(mobile)
#             mobile=int(mobile)+1
#         response = self.user.httpJhjSmsRegisterJson(mobile_list[0])
#         self.assertEqual(200,response['code'],msg=u"响应返回状态异常")
#
#
#     def testHttpJhjSmsRegisterJson002(self):
#         """注册发送验证码---已注册账号"""
#         mobile = self.data['mobile2']
#         mobile_list=[]
#         while len(mobile_list)!=1:
#             if SqlMember().member(mobile)!=None:
#                 mobile_list.append(mobile)
#             mobile=int(mobile)+1
#         response = self.user.httpJhjSmsRegisterJson(mobile_list[0])
#         self.assertEqual(200,response['code'],msg=u"响应返回状态异常")
#
#
#     def testHttpJhjRegisterJson001(self):
#         """注册账号---未注册的手机号"""
#         mobile = self.data['mobile3']
#         password = self.data['password3']
#         mobile_list=[]
#         while len(mobile_list)!=1:
#             if SqlMember().member(mobile)==None:
#                 mobile_list.append(mobile)
#             mobile=int(mobile)+1
#         response = self.user.httpJhjRegisterJson(mobile_list[0],password)
#         self.assertEqual(200,response['code'],msg=u"响应返回状态异常")
#         self.assertEqual(mobile_list[0],response['data']['mobile'],msg=u"响应返回数据异常")
#
#     def testHttpJhjRegisterJson002(self):
#         """注册账号---密码为空"""
#         mobile = self.data['mobile4']
#         password = ''
#         mobile_list=[]
#         while len(mobile_list)!=1:
#             if SqlMember().member(mobile)==None:
#                 mobile_list.append(mobile)
#             mobile=int(mobile)+1
#         response = self.user.httpJhjRegisterJson(mobile_list[0],password)
#         self.assertEqual(200,response['code'],msg=u"响应返回状态异常")
#         self.assertEqual(mobile_list[0],response['data']['mobile'],msg=u"响应返回数据异常")
#
#
#     def testHttpJhjLoginByCodeJson001(self):
#         """验证码登录---已注册的手机号"""
#         mobile = self.data['mobile5']
#         response = self.user.httpJhjLoginByCodeJson(mobile)
#         self.assertEqual(200,response['code'],msg=u"响应返回状态异常")
#         self.assertEqual(mobile,response['data']['mobile'],msg=u"响应返回数据异常")
#
#     def testHttpJhjLoginByCodeJson002(self):
#         """验证码登录---未注册的手机号"""
#         mobile = self.data['mobile6']
#         response = self.user.httpJhjLoginByCodeJson(mobile)
#         self.assertEqual(200,response['code'],msg=u"响应返回状态异常")
#         self.assertEqual(mobile,response['data']['mobile'],msg=u"响应返回数据异常")
#
#     def testHttpJhjSmsFindLoginPasswordJson(self):
#         """找回密码,发送验证码"""
#         mobile = self.data['mobile7']
#         response = self.user.httpJhjSmsFindLoginPasswordJson(mobile)
#         self.assertEqual(200,response['code'],msg=u"响应返回状态异常")
#
#     def testHttpJhjUserPasswordFindPasswordJson001(self):
#         """"找回密码登录"""
#         mobile = self.data['mobile8']
#         setPassword = self.data['mobile8']
#         response = self.user.httpJhjUserPasswordFindPasswordJson(mobile,setPassword)
#
#     def testHttpJhjUserPasswordFindPasswordJson002(self):
#         """"找回密码登录---密码为空"""
#         mobile = self.data['mobile9']
#         setPassword = ''
#         response = self.user.httpJhjUserPasswordFindPasswordJson(mobile,setPassword)
#
#
#     def testHttpJhjLoginJson001(self):
#         """账号密码登录---正确的账号和密码"""
#         mobile = self.data['mobile10']
#         password = self.data['password10']
#         response = self.user.httpJhjLoginJson(mobile,password)
#
#     def testHttpJhjLoginJson002(self):
#         """账号密码登录---正确的账号,错误的密码"""
#         mobile = self.data['mobile11']
#         password = self.data['password11']
#         response = self.user.httpJhjLoginJson(mobile,password)
#
#     def testHttpJhjLoginJson003(self):
#         """账号密码登录---正确的账号,密码为空"""
#         mobile = self.data['mobile12']
#         password = ''
#         response = self.user.httpJhjLoginJson(mobile,password)
#
#     def testHttpJhjLoginJson004(self):
#         """账号密码登录---账号和密码都为空"""
#         mobile = self.data['mobile13']
#         password = ''
#         response = self.user.httpJhjLoginJson(mobile,password)
#
#     def testHttpJhjLoginJson005(self):
#         """账号密码登录---企业投资人登录"""
#         mobile = self.data['mobile14']
#         password = self.data['password14']
#         response = self.user.httpJhjLoginJson(mobile,password)
#
#     def testHttpJhjLoginJson006(self):
#         """账号密码登录---合作机构登录"""
#         mobile = self.data['mobile15']
#         password = self.data['password15']
#         response = self.user.httpJhjLoginJson(mobile,password)
#
#     def testHttpJhjLoginJson007(self):
#         """账号密码登录---担保机构登录"""
#         mobile = self.data['mobile16']
#         password = self.data['password16']
#         response = self.user.httpJhjLoginJson(mobile,password)
#
#     def testHttpJhjLoginJson008(self):
#         """账号密码登录---借款机构登录"""
#         mobile = self.data['mobile17']
#         password = self.data['password17']
#         response = self.user.httpJhjLoginJson(mobile,password)
#
#     def testHttpJhjLoginJson009(self):
#         """账号密码登录---供应商登录"""
#         mobile = self.data['mobile18']
#         password = self.data['password18']
#         response = self.user.httpJhjLoginJson(mobile,password)
#
# if __name__ == '__main__':
#     unittest.main()
#
#
#
