# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2018/4/9 15:38
from public.publicLogs import PublicLogs
log = PublicLogs()
import MySQLdb,re
class SqlMessage:
    def message(self,mobile):
        """
        获取验证码
        :param sql:
        :return:
        """
        db=MySQLdb.connect(

        )
        cursor = db.cursor()
        cursor.execute("select * from t_sms where Mobile='%s' order by Id DESC"%mobile)

        '''
        1获取第一条查询结果
        2拿到content信息,也就是通过索引3获取
        3正则拿到验证码
        '''
        result_sql= cursor.fetchone()
        result_message=result_sql[3]
        r=re.compile(r'\d+')

        res1=re.search(r,result_message)
        cursor.close()
        #关闭
        db.close()
        try:
            return res1.group(0)
        except:
            log.info(u"验证码发送失败,请确认")
if  __name__ == '__main__':
    sql=SqlMessage()
    print sql.message(17007700002)
    # 17000008888




