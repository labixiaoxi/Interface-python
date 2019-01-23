# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2018/4/2 16:18
import hashlib
class PublicMd5:
    def md5(self,key):
        result=hashlib.md5()
        result.update(key)
        result_code=result.hexdigest()
        return result_code

if __name__== '__main__':
    m=PublicMd5()
    print m.md5('')


