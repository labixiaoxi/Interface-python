# *_*coding:utf-8 *_*
import requests
from public.publicLogs import PublicLogs
from public.publicMd5 import PublicMd5
from public.publicYaml import PublicGetYaml
from sql.sqlMessage import SqlMessage
from httpAPI.httpMethod import HttpMethod
log = PublicLogs()

class HttpUserAPI:
    def __init__(self,yamlUserPath):
        self.uri=PublicGetYaml(yamlUserPath).get_Yaml()['user']['uri']
        self.message = SqlMessage()
        self.md5=PublicMd5()

    def httpJhjSmsRegisterJson(self,mobile):
        """
        发送验证码
        :return:
        """
        self.url="/jhj/sms/register.json"
        self.data={
            "sign":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiIxNzc3MDAwMDMwMiJ9.1NQ2mf39ICLYk80XHPZdHKH9fF4sfpMTyzqZsLmd-sU",
            "mobile":mobile
        }
        return HttpMethod(self.uri,self.url,self.data).http_post()


    def httpJhjRegisterJson(self,mobile,password):
        """
        注册
        :return:
        """
        self.httpJhjSmsRegisterJson(mobile)
        code =self.message.message(mobile)
        self.url="/jhj/register.json"
        self.data={
            "password":self.md5.md5(password),
            "sign":"",
            "code":code,
            "mobile":mobile,
            "mac":""
        }
        return HttpMethod(self.uri,self.url,self.data).http_post()

    def httpJhjLoginByCodeJson(self,mobile):
        """
        验证码登录
        :param mobile:
        :return:
        """
        self.httpJhjSmsRegisterJson(mobile)
        code =self.message.message(mobile)
        self.url="/jhj/loginByCode.json"
        self.data={
            "sign":"",
            "mobile":mobile,
            "code":code,
            "mac":""
        }
        return HttpMethod(self.uri,self.url,self.data).http_post()

    def httpJhjSmsFindLoginPasswordJson(self,mobile):
        """
        找回密码发送验证码
        :return:
        """
        self.url="/jhj/sms/findLoginPassword.json"
        self.data={
            "mobile":mobile,
            "sign":""
        }
        return HttpMethod(self.uri,self.url,self.data).http_post()

    def httpJhjUserPasswordFindPasswordJson(self,mobile,setpassword):
        """
        找回密码登录
        :param mobile:
        :param setpassword:
        :return:
        """
        self.httpJhjSmsFindLoginPasswordJson(mobile)
        code =self.message.message(mobile)
        self.url="/jhj/user/password/findPassword.json"
        self.data={
            "loginPwd":self.md5.md5(setpassword),
            "code":code,
            "mobile":mobile,
            "sign":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblB3ZCI6IjY1NjVlNDJhNjQzMWNkMTY1NWRlMDBiYWZjYmM0MmZmIiwibW9iaWxlIjoiMTc3NzAwMDAzMDIiLCJjb2RlIjoiMzk2OTE2In0.O0hQoLkTDdeiAT0oZMKCXKHyVjBbT41h01COvoB6JfE"
        }
        return HttpMethod(self.uri,self.url,self.data).http_post()

    def httpJhjLoginJson(self,mobile,password):
        """
        账号密码登录
        :param mobile:
        :param password:
        :return:
        """
        self.url="/jhj/login.json"
        self.data={
            "sign":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6IjY1NjVlNDJhNjQzMWNkMTY1NWRlMDBiYWZjYmM0MmZmIiwibW9iaWxlIjoiMTc3NzAwMDAzMDIiLCJtYWMiOiI5MGQwMmFjZDJhMGY0MWQ4In0.a5jXWZUK1kSE5Vs7arBCJlgBX_9l_Q42NqLD2oU8pFc",
            "mobile":mobile,
            "password":self.md5.md5(password),
            "mac":"90d02acd2a0f41d8"
        }
        return HttpMethod(self.uri,self.url,self.data).http_post()

    def d(self):
        print "d"


if __name__ == '__main__':
    path = '../../yamlData/yamlUser.yaml'
    http = HttpUserAPI(path)
    print http.httpJhjRegisterJson('17770077778','xiaoxi123')


