# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import sqlite3
import mysql.connector


class FirstWebSpiderPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        # self.conn = sqlite3.connect("myquotes.db")
        # self.curr = self.conn.cursor()
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='63398049nty',
            database='myquotes'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""create table quotes_tb(
                        title text,
                        author text,
                        tag text
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        if len(item['tag']) == 0:
            item['tag'] = ['Nothing displayed']
        # for singleItem in [item['title'], item['author'], item['tag']]:
        #     if len(singleItem) == 0:
        #         singleItem = ['Nothing displayed on the webside']

        self.curr.execute("""insert into quotes_tb values (%s, %s, %s)""", (
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()
