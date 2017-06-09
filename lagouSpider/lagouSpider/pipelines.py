# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi

# class MysqlTwistedPipeline(object):
#     def __init__(self,dbpool):
#         #会获取到链接池实例化
#         self.dbpool = dbpool
#
#     @classmethod
#     def from_settings(cls,settings):
#         #读取数据库参数并且产生连接池实例
#         dbparms = dict(
#             host = settings['MYSQL_HOST'],
#             port = settings['MYSQL_PORT'],
#             user = settings['MYSQL_USER'],
#             password = settings['MYSQL_PASSWORD'],
#             database = settings['MYSQL_DB'],
#             charset = settings['MYSQL_ENCODING'],
#             use_unicode = True,
#             #cursorclass=pymysql.cursors.DictCursor
#         )
#         dbpool = adbapi.ConnectionPool('pymysql',**dbparms)
#         return cls(dbpool)
#
#     def process_item(self, item, spider):
#         #异步化操作
#         query = self.dbpool.runInteraction(self.do_insert,item)
#         query.addErrback(self.handle_error,item,spider)
#         return item
#
#     def handle_error(self,failure,item,spider):
#         #处理异步插入的异常
#         print(failure)
#
#     def do_insert(self,cursor,item):
#         #执行具体的插入操作
#         insert_sql, params = item.get_insert_sql()
#         print('爬取：' + params[0] + '成功，正在写入数据库...')
#         cursor.execute(insert_sql, params)

import pymysql
class MysqlPipeline(object):
    #数据库同步操作
    def __init__(self,mysql_settings):
        self.conn = pymysql.connect(host=mysql_settings['MYSQL_HOST'],port=mysql_settings['MYSQL_PORT'],user=mysql_settings['MYSQL_USER'],password=mysql_settings['MYSQL_PASSWORD'],db=mysql_settings['MYSQL_DB'],charset='utf8mb4')
        self.cursor = self.conn.cursor()

    @classmethod
    def from_settings(cls, settings):
        mysql_settings = dict(
            MYSQL_HOST = settings['MYSQL_HOST'],
            MYSQL_PORT = settings['MYSQL_PORT'],
            MYSQL_USER = settings['MYSQL_USER'],
            MYSQL_PASSWORD = settings['MYSQL_PASSWORD'],
            MYSQL_DB = settings['MYSQL_DB']
        )
        return cls(mysql_settings)

    def process_item(self,item,spider):
        insert_sql, params = item.get_insert_sql()
        with self.conn.cursor() as cursor:
            cursor.execute(insert_sql, params)
            print('爬取：' + params[0] + '成功，正在写入数据库...')
            self.conn.commit()
