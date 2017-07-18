# -*- coding: utf-8 -*-
import scrapy
import json
import time
from kc.items import KcItem
from kc.utils.get import get_key


class KuchuanSpider(scrapy.Spider):
	name = 'kuchuan'
	down_url = 'http://android.kuchuan.com/totaldownload?packagename={app_package}&date={now}'
	trend_url = 'http://android.kuchuan.com/histortytotaldownload?packagename={app_package}&start_date=&end_date=&longType=3-m&date={now}'

	def start_requests(self):
		# while True:
		# 	id_app_package = get_key('id_app_package')
			id_app_package = '136824~air.com.invisibleowl.tattooyourselfcamera'
			# if not id_app_package:
			# 	continue
			lis = id_app_package.split('~')
			id = int(lis[0])
			app_package = lis[1]
			item = KcItem()
			item['id'] = id
			item['app_package'] = app_package
			self.url1 = self.down_url.format(app_package=app_package, now=int(time.time()) * 1000)
			yield scrapy.Request(self.url1, meta={'item': item, 'dont_redirect': True}, dont_filter=True)

	def parse(self, response):
		item = response.meta.get('item', '')
		if not item:
			return
		app_package = item['app_package']
		# down = item.get('down', '')
		text = response.text
		# if down:
		# 	# 如果有down，说明1爬了，返回的是2的结果，
		# 	if response.text:
		# 		item['trend'] = text
		# 	else:
		# 		item['trend'] = 'none'
		# else:
		# 	# 如果没有down，说明1还没爬，将text交给down，并请求2
		if text:
			item['down'] = text
			print(item['down'][:50])
		else:
			item['down'] = ''
		self.url2 = self.trend_url.format(app_package=app_package, now=int(time.time()) * 1000)
		yield scrapy.Request(self.url2, meta={'item': item, 'dont_redirect': True}, dont_filter=True,
		                     callback=self.parse_trend)

	def parse_trend(self, response):
		item = response.meta.get('item', '')
		if not item:
			return
		if response.text:
			item['trend'] = response.text
		else:
			item['trend'] = ''

		return item