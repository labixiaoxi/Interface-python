# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2018/4/9 15:38
import MySQLdb,re
class SqlProduct:
    def product(self,sql):
        db=MySQLdb.connect(

        )
        cursor = db.cursor()
        cursor.execute(sql)
        result_sql= cursor.fetchall()
        cursor.close()
        db.close()
        # 查询没有结果返回None

        if result_sql == None:
            return 0
        else:
            return result_sql
if  __name__ == '__main__':
    sql=SqlProduct()
    print sql.product("select * from product where category=2 and sell_end_time>=(SELECT DATE_FORMAT(NOW(),'%Y-%m-%d %H:%i:%S'))")




