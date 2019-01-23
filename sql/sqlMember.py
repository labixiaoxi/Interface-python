# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2018/4/9 15:38
import MySQLdb,re
class SqlMember:
    def member(self,mobile):
        """
        判断账号是否注册
        :param sql:
        :return:
        """
        db=MySQLdb.connect(

        )
        cursor = db.cursor()
        cursor.execute("select * from t_member where mobile='%s'"%mobile)
        result_sql= cursor.fetchone()
        cursor.close()
        db.close()
        # 查询没有结果返回None
        if result_sql == None:
            return result_sql
        else:
            return result_sql[0]
if  __name__ == '__main__':
    sql=SqlMember()
    print sql.member(17770007710)




