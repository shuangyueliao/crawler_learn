# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import MySQLdb
import datetime
 
DEBUG = True
 
if DEBUG:
    dbuser = 'root'
    dbpass = '123456'
    dbname = 'game_main'
    dbhost = '127.0.0.1'
    dbport = '3306'
else:
    dbuser = 'root'
    dbpass = '123456'
    dbname = 'game_main'
    dbhost = '127.0.0.1'
    dbport = '3306'
     
class MySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE `news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  `addtime` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=901 DEFAULT CHARSET=utf8;''')
        #清空表：
        self.cursor.execute("truncate table news;")
        self.conn.commit() 
         
    def process_item(self, item, spider): 
        try:
            self.cursor.execute("""INSERT INTO news(title, link, addtime)  
                            VALUES (%s, %s, %s)""", 
                            (
                                item['title'][0].encode('utf-8'), 
                                item['link'][0].encode('utf-8'),
                                item['addtime'][0].encode('utf-8'),
                            )
            )
     
            self.conn.commit()
     
     
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item