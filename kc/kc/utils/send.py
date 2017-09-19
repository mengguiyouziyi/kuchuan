# coding:utf-8

import os
import sys
import time
from datetime import datetime
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
		本机 localhost；公司 etl2.innotree.org；服务器 etl1.innotree.org
		"""
	mysql = pymysql.connect(host='etl1.innotree.org', port=3308, user='spider', password='spider', db='spider', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	# mysql = pymysql.Connect(host='localhost', user='root', password='3646287', db='spiders', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	try:
		with mysql.cursor() as cursor:
			# input-time=‘2017-07-20’
			sql = """select id, sapp_pkgname from kuchuan_down"""
			# sql = """select id, app_package from kuchuan_all where down like '%script%'"""
			print('execute begain')
			cursor.execute(sql)
			results = cursor.fetchall()
			values = [str(i['id']) + '~' + i['sapp_pkgname'].strip() for i in results]
	finally:
		mysql.close()

	red = QueueRedis()

	if values:
		for i, value in enumerate(values):
			red.send_to_queue(key, value)


if __name__ == '__main__':
	# while True:
	send_key(key='id_app_package')
		# print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		# print('tomorrow go on~~~')
		# time.sleep(86400)
