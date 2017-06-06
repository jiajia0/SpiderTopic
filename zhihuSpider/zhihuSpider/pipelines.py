# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi

class ZhihuspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlTwistedPipeline(object):
    def __init__(self,dbpool):
        #会获取到链接池实例化
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):
        #读取数据库参数并且产生连接池实例
        dbparms = dict(
            host = settings['MYSQL_HOST'],
            port = settings['MYSQL_PORT'],
            user = settings['MYSQL_USER'],
            password = settings['MYSQL_PASSWORD'],
            database = settings['MYSQL_DB'],
            charset = settings['MYSQL_ENCODING'],
            use_unicode = True,
            #cursorclass=pymysql.cursors.DictCursor
        )
        dbpool = adbapi.ConnectionPool('pymysql',**dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        #异步化操作
        query = self.dbpool.runInteraction(self.do_insert,item)
        query.addErrback(self.handle_error,item,spider)
        return item

    def handle_error(self,failure,item,spider):
        #处理异步插入的异常
        print(failure)

    def do_insert(self,cursor,item):
        #执行具体的插入操作
        insert_sql, params = item.get_insert_sql()
        print('爬取：' + params[3] + '成功，正在写入数据库...')
        cursor.execute(insert_sql, params)


