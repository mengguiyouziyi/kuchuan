# coding:utf-8

import os
import sys
from os.path import dirname

import pymysql
from my_redis import QueueRedis

# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

father_path = os.path.abspath(dirname(__file__))
sys.path.append(father_path)


def send_key(key):
	"""
	ids:123,234,234, quan_cheng:美团，百度
	"""
	mysql = pymysql.connect(host='etl1.innotree.org', user='spider', password='spider', db='spider', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	# mysql = pymysql.Connect(host='localhost', user='root', password='3646287', db='spiders', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	try:
		with mysql.cursor() as cursor:
			sql = """select id, app_package from wandoujia_app_info ORDER BY id"""
			cursor.execute(sql)
			print('execute begain')
			results = cursor.fetchall()
			values = [str(i['id']) + '~' + i['app_package'].strip() for i in results]
	finally:
		mysql.close()

	red = QueueRedis()

	if values:
		for i, value in enumerate(values):
			print(i+1)
			red.send_to_queue(key, value)


if __name__ == '__main__':
	send_key(key='id_app_package')
