# -*- coding: utf-8 -*-
# @Time    : 2018-09-21-上午11:47
# @Author  : lindozy
# @File    : dbUtils.py
# @Software: PyCharm
import pymysql
from settings import *


class GetDataFromMySql:
    def __init__(self):
        try:
            self.conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
        except Exception as e:
            print(e)
        else:
            print('连接成功！')
            self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def query(self, args):
        sql = f'select * from {table}'
        self.cur.execute(sql)
        rs = self.cur.fetchall()
        return rs

    def update(self, args):
        #添加判断条件
        sql = f'update {table} set is_dl=1 where url={args}'
        rs = self.cur.execute(sql)
        if rs:
            self.conn.commit()
            print('更新成功!')
        else:
            self.conn.rollback()
            print('更新失败！')

class GetDataFromExcel:
    pass


if __name__ == '__main__':
    m = GetDataFromMySql()
    rs = m.query(table)
    for i in rs:
        print(i)
