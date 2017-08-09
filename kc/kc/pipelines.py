# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class MysqlPipeline(object):
	"""
	本机 localhost；公司 etl2.innotree.org；服务器 etl1.innotree.org
	"""
	def __init__(self):
		self.conn = pymysql.connect(host='etl1.innotree.org', port=3308, user='spider', password='spider', db='spider', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
		# self.conn = pymysql.connect(host='localhost', user='root', password='3646287', db='spider', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		if spider.name == 'kuchuan':
			# sql = """insert into kuchuan_all(id, app_package, down, trend) VALUES(%s, %s, %s, %s) ON DUPLICATE KEY UPDATE app_package=VALUES(app_package), down=VALUES(down), down=VALUES(trend)"""
			sql = """replace into kuchuan_all_copy(id, app_package, down, trend, crawl_time) VALUES(%s, %s, %s, %s, %s)"""
			args = (item["id"], item["app_package"], item["down"], item["trend"], item["crawl_time"])
			self.cursor.execute(sql, args=args)
			self.conn.commit()
			print(str(item['id']) + ' success')
		elif spider.name == 'kuchuan_daily':
			sql = """insert into kuchuan_down_num(app_package, down_num, crawl_time) VALUES(%s, %s, %s)"""
			args = (item["app_package"], item["down_num"], item["crawl_time"])
			self.cursor.execute(sql, args=args)
			self.conn.commit()
			print(str(item['app_package']) + ' success')