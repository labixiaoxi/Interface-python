# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/22 15:33
import unittest,os,time,HTMLTestRunner
case_path = os.path.join(os.getcwd(), "testHttpAPI")
discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
if __name__ == "__main__":
    now = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
    report_path = os.path.join(os.getcwd(), now+".html")
    fp=open(report_path,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                        title=u'用例执行情况',
                        description=u'金惠家理财接口:')
    runner.run(discover)
    fp.close()

