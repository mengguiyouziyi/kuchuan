# -*- coding: utf-8 -*-
import scrapy
import time
import json
from scrapy.exceptions import CloseSpider
from datetime import datetime
from kc.items import KcItem
from kc.utils.get import get_key
from kc.settings import SQL_DATETIME_FORMAT


class KuchuanSpider(scrapy.Spider):
	name = 'kuchuan_daily'
	# daily_url = 'http://android.kuchuan.com/dailydownload?packagename=com.demofarms.timesheet&status=0&date=1502262567178'
	daily_url = 'http://android.kuchuan.com/dailydownload?packagename={app_package}&status=-1&date={now}'

	def start_requests(self):
		# ls = ['145819~com.leaguestat.lsmobileappringettecanada', '148145~com.sarawut.kidsdrawingofdinosaurs', '152953~com.sixtyfourthirtytwo.terra', '153881~com.zzzz.hamidou', '158748~com.apptreestudios.gravityglasshit', '160232~com.assistance', '214602~fr.yeast', '238474~hksarg.bd.mwcs', '269911~com.sp2p.SXYG', '290994~com.phonedeco.themecontents.theme_10000049', '294626~com.magook.kind8_198', '339048~com.ecmoban.android.gflmall', '339300~com.ecpalm.parenting.android', '339861~com.editorphotowahey.photoeditorcutpast', '408347~com.babywhere.babyanimals', '418867~zm.mobile.zongbuzhizuobu767598', '442641~com.brodev.socialapp.urbangroweronline', '522768~cityguide.Graz', '560740~com.jsjwdx.jwnw', '581072~com.jh.APP5f44dd862a8d4d2ca3a89701af611638.news', '619191~com.platoevolved.dressupkitty', '619250~com.platomix.mobileenterprise112', '653283~com.lianyun.jiaju', '664626~com.kxmzlyhg.chuangyidabaike', '670672~com.radio.station.KXTG.AM', '770295~com.vinzstudios.Box_Appraiser_DGM_Edition', '849332~com.yk.cosmo']
		# for l in ls:
		x = 0
		while True:
			id_app_package = get_key('id_app_package')
			# id_app_package = '0~com.aa.generaladaptiveapps'
			if not id_app_package:
				x += 1
				if x > 5:
					raise CloseSpider('no datas')
				time.sleep(60)
				continue
			lis = id_app_package.split('~')
			# id = int(lis[0])
			app_package = lis[1]
			item = KcItem()
			# item['id'] = id
			item['app_package'] = app_package
			self.url = self.daily_url.format(app_package=app_package, now=int(time.time()) * 1000)
			yield scrapy.Request(self.url, meta={'item': item, 'dont_redirect': True}, dont_filter=True)

	def parse(self, response):
		item = response.meta.get('item', '')
		if not item:
			return
		"""
		{"status":200, "msg":"请求成功", "data":{"豌豆荚":19,"360":""}}
		{"status":200, "msg":"请求成功", "data":{"联想":294,"OPPO":24,"vivo":6993}}
		"""
		# text = json.loads(response.text) if response.text else ''
		data = json.loads(response.text)['data'] if '请求成功' in response.text else {}
		nums_unknown = data.values() if data else []
		nums = [num for num in nums_unknown if isinstance(num, int)]
		item['down_num'] = sum(nums)

		item["crawl_time"] = datetime.now().strftime(SQL_DATETIME_FORMAT)
		# print(item['trend'][:50])

		return item