# -*- coding: utf-8 -*-
import scrapy
import time
import datetime
from kc.items import KcItem
from kc.utils.get import get_key
from kc.settings import SQL_DATETIME_FORMAT, SQL_DATE_FORMAT


class KuchuanSpider(scrapy.Spider):
	name = 'kuchuan'
	down_url = 'http://android.kuchuan.com/totaldownload?packagename={app_package}&date={now}'
	trend_url = 'http://android.kuchuan.com/histortytotaldownload?packagename={app_package}&start_date=&end_date=&longType=3-m&date={now}'

	def start_requests(self):
		# ls = ['145819~com.leaguestat.lsmobileappringettecanada', '148145~com.sarawut.kidsdrawingofdinosaurs', '152953~com.sixtyfourthirtytwo.terra', '153881~com.zzzz.hamidou', '158748~com.apptreestudios.gravityglasshit', '160232~com.assistance', '214602~fr.yeast', '238474~hksarg.bd.mwcs', '269911~com.sp2p.SXYG', '290994~com.phonedeco.themecontents.theme_10000049', '294626~com.magook.kind8_198', '339048~com.ecmoban.android.gflmall', '339300~com.ecpalm.parenting.android', '339861~com.editorphotowahey.photoeditorcutpast', '408347~com.babywhere.babyanimals', '418867~zm.mobile.zongbuzhizuobu767598', '442641~com.brodev.socialapp.urbangroweronline', '522768~cityguide.Graz', '560740~com.jsjwdx.jwnw', '581072~com.jh.APP5f44dd862a8d4d2ca3a89701af611638.news', '619191~com.platoevolved.dressupkitty', '619250~com.platomix.mobileenterprise112', '653283~com.lianyun.jiaju', '664626~com.kxmzlyhg.chuangyidabaike', '670672~com.radio.station.KXTG.AM', '770295~com.vinzstudios.Box_Appraiser_DGM_Edition', '849332~com.yk.cosmo']
		# for l in ls:
		while True:
			id_app_package = get_key('id_app_package')
			# id_app_package = l
			if not id_app_package:
				continue
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
		print(item['id'])
		print(app_package)
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
			# print(item['down'][:50])
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
		item["crawl_time"] = datetime.now().strftime(SQL_DATETIME_FORMAT)
		print(item['trend'][:50])


		return item