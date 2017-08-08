# coding:utf-8

import pymysql
import json


def get_json():
	mysql = pymysql.connect(host='etl1.innotree.org', port=3308, user='spider', password='spider', db='spider', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	# mysql = pymysql.Connect(host='localhost', user='root', password='3646287', db='spiders', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	try:
		with mysql.cursor() as cursor:
			sql = """select id, app_package, down from kuchuan_all_copy ORDER by id"""
			# sql = """select id, app_package from kuchuan_all where down like '%"categories"%' and id < 140000"""
			print('execute begain')
			cursor.execute(sql)
			results = cursor.fetchall()

			for result in results:
				try:
					id = result.get('id')
					print(id)
					app_package = result.get('app_package')
					down = json.loads(result.get('down', ''))

					data = down.get('data', '')
					if data:
						x = list(data.values())
						down_total = sum(x)
					else:
						down_total = 0

					in_sql = """replace into kuchuan_all_down_copy(id, app_package, down_total) value(%s, %s, %s)"""

					cursor.execute(in_sql, (id, app_package, down_total))
					mysql.commit()
				except Exception as e:
					print(e)
					continue
	except Exception as e:
		print(e)
		pass
	finally:
		mysql.close()


if __name__ == '__main__':

    get_json()




































"""
			<class 'list'>: [{'id': 134425, 'app_package': 'a2z.Mobile.AAPEX', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":747}}'}, {'id': 134426, 'app_package': 'a2z.Mobile.Event2402', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":421}}'}, {'id': 134427, 'app_package': 'a2z.Mobile.Event2618', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":409}}'}, {'id': 134428, 'app_package': 'a2z.Mobile.NSHMBA2013', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":1078}}'}, {'id': 134429, 'app_package': 'aa123.bb123.cc123', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134430, 'app_package': 'aaa123.sss123.ddd123', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134431, 'app_package': 'aa.english.spanish.french.lock', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":300,"360":1}}'}, {'id': 134432, 'app_package': 'aaos.xlite2012', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":650,"OPPO":265,"百度":843,"360":15}}'}, {'id': 134433, 'app_package': 'aaos.xlite2013', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":725,"vivo":1000}}'}, {'id': 134434, 'app_package': 'com.candydev.csc', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134435, 'app_package': 'com.candydev.enzz', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134436, 'app_package': 'com.candydev.gdm', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134437, 'app_package': 'com.candydev.str', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134438, 'app_package': 'com.candydev.und', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134439, 'app_package': 'com.CandyGaming.SpeedyRace', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134440, 'app_package': 'com.candykingdoms.bakerystory', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134441, 'app_package': 'com.candykingdoms.candysogamania', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134442, 'app_package': 'com.candylegend.legend', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134443, 'app_package': 'com.candyLips.MakeoverGirls', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134444, 'app_package': 'com.candy.lollipop.crush.cookie.jam.free', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134445, 'app_package': 'com.can.listen', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":543}}'}, {'id': 134446, 'app_package': 'com.cannae.snooker', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":180,"OPPO":787,"360":30}}'}, {'id': 134447, 'app_package': 'aaos.xlite2014', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":493,"vivo":1000,"360":4}}'}, {'id': 134448, 'app_package': 'com.cannae.woodhouse', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":770}}'}, {'id': 134449, 'app_package': 'aastudios.ilight', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":563,"vivo":6}}'}, {'id': 134450, 'app_package': 'com.canny.PlantarFasciitis', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":1075,"360":1}}'}, {'id': 134451, 'app_package': 'com.canteratech.chitchat.sme2013', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":978,"360":7}}'}, {'id': 134452, 'app_package': 'aa.wdpg', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":860,"应用宝":7,"360":3}}'}, {'id': 134453, 'app_package': 'com.canvas.bike.racing.dino.adventure', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134454, 'app_package': 'aax.uab.quiztallography', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134455, 'app_package': 'com.canvasm.fightback', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":615,"OPPO":34,"360":12}}'}, {'id': 134456, 'app_package': 'abc.mskido.hollykids', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134457, 'app_package': 'abdo.shot.balle', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134458, 'app_package': 'com.caohua.xqzlr.uc', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134459, 'app_package': 'abshahin.oyun.yarishaq.herfler', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":1020,"百度":8204}}'}, {'id': 134460, 'app_package': 'abstractflowers.liveWPcube', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":146,"360":1}}'}, {'id': 134461, 'app_package': 'ab.studying.simplemath', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":1054}}'}, {'id': 134462, 'app_package': 'com.caosdevelopers.app_pdapersonal', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":78,"OPPO":505,"360":226}}'}, {'id': 134463, 'app_package': 'abwin.dashboard', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":185}}'}, {'id': 134464, 'app_package': 'com.CapitalJProductionz.com.BasketBaller', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134465, 'app_package': 'com.captain.underppants.game', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134466, 'app_package': 'accessoryshop.app', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":3210}}'}, {'id': 134467, 'app_package': 'acebridge.android', 'down': '{"status":200, "msg":"请求成功", "data":{"联想":5000,"豌豆荚":25000,"OPPO":210733,"百度":226221,"应用宝":212953,"vivo":3854,"360":867516}}'}, {'id': 134468, 'app_package': 'ace.bubble', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134469, 'app_package': 'achute.pixelsnake', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134470, 'app_package': 'ac.intaj', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":774,"360":2}}'}, {'id': 134471, 'app_package': 'com.captive.princessmakeuplite', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":341000,"百度":110927,"应用宝":638}}'}, {'id': 134472, 'app_package': 'acm.mainactivity', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":153,"360":6}}'}, {'id': 134473, 'app_package': 'com.cryms.eso', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":925,"vivo":2,"360":8}}'}, {'id': 134474, 'app_package': 'acm.patio2012', 'down': '{"status":200, "msg":"请求成功", "data":{"360":1}}'}, {'id': 134475, 'app_package': 'com.crystalhotels', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":772}}'}, {'id': 134476, 'app_package': 'com.CrystallineGreen.OceanMining', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134477, 'app_package': 'a.c.sqlite_test_102m06014', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":575}}'}, {'id': 134478, 'app_package': 'com.capuzzello.summercountdown', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134479, 'app_package': 'com.crystaltreecc', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":717}}'}, {'id': 134480, 'app_package': 'com.caqigyb.sherbwio', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134481, 'app_package': 'actions.wwe.extreme', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134482, 'app_package': 'com.carabellijuliet.tetrisdeh', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134483, 'app_package': 'com.crysware', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":901,"应用宝":2,"360":6}}'}, {'id': 134484, 'app_package': 'ada.aeroinha.aerodyn', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":390}}'}, {'id': 134485, 'app_package': 'adamitech.br', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":930}}'}, {'id': 134486, 'app_package': 'com.CSC.CaveRush', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134487, 'app_package': 'com.csdd.sbwsw.mi', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134488, 'app_package': 'com.cseg.ut', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134489, 'app_package': 'adamtorok.densityconverter', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":374}}'}, {'id': 134490, 'app_package': 'adec.andro.openrdk.arc', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":340,"360":13}}'}, {'id': 134491, 'app_package': 'com.cara.diet.golongan.darah', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":982}}'}, {'id': 134492, 'app_package': 'ad.en.world.war1942', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":1036}}'}, {'id': 134493, 'app_package': 'com.caramelizedapple.apps.PicassoC', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":4680,"百度":5128,"应用宝":138,"360":6863}}'}, {'id': 134494, 'app_package': 'com.carbonicdigital.Dota2HerosSounds', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":481,"360":39}}'}, {'id': 134495, 'app_package': 'com.csgames.animal.hunting.season', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134496, 'app_package': 'adinfo.adinfoveerzaara.veerzaara', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":577}}'}, {'id': 134497, 'app_package': 'com.car.carrun', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134498, 'app_package': 'com.csg.ewccodes', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":42,"360":5}}'}, {'id': 134499, 'app_package': 'adora.earth', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":348,"vivo":10,"360":2}}'}, {'id': 134500, 'app_package': 'com.cardeliverynetwork', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":875,"百度":599}}'}, {'id': 134501, 'app_package': 'com.card.emotion.argo.cn', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":994,"百度":278,"应用宝":26,"360":7}}'}, {'id': 134502, 'app_package': 'com.csie102406049', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134503, 'app_package': 'adsID.bisnis.ukm.apps', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":53}}'}, {'id': 134504, 'app_package': 'adsprotech.games.hidden.object.game', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134505, 'app_package': 'com.cardgame.solitaire.castlephantom', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134506, 'app_package': 'com.cs.iphone.ilock.locker.htc.droid.dna', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":598}}'}, {'id': 134507, 'app_package': 'com.cs.iphone.ilock.locker.samsung.galaxy.note', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":105}}'}, {'id': 134508, 'app_package': 'ae.adfca.adfca_pub', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":385}}'}, {'id': 134509, 'app_package': 'com.csndoi.poiwe.der', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134510, 'app_package': 'aero.kerozen', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":90,"360":3}}'}, {'id': 134511, 'app_package': 'com.css.babysteps', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134512, 'app_package': 'afteryou.Jarvis', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":238,"360":63}}'}, {'id': 134513, 'app_package': 'com.csscorp.activei2', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":310,"360":1}}'}, {'id': 134514, 'app_package': 'com.cardgames.skipit', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134515, 'app_package': 'agario.skins.game', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134516, 'app_package': 'com.invogue.Fidget', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134517, 'app_package': 'com.csscorp.gearhead', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":1140,"OPPO":68,"应用宝":267}}'}, {'id': 134518, 'app_package': 'ago.violinpitchpipe', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":504,"应用宝":24,"vivo":2,"360":7}}'}, {'id': 134519, 'app_package': 'com.Cardiff.CardiffRFC', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":995}}'}, {'id': 134520, 'app_package': 'agriprecision.pck', 'down': '{"status":200, "msg":"请求成功", "data":{"360":2}}'}, {'id': 134521, 'app_package': 'com.cardmaster.coloringbookgame', 'down': '{"status":200, "msg":"请求成功", "data":{}}'}, {'id': 134522, 'app_package': 'com.invoiceapp', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":579,"360":1}}'}, {'id': 134523, 'app_package': 'com.CSTipCalculator.tipcalculator', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":703}}'}, {'id': 134524, 'app_package': 'com.cardola.mayfair', 'down': '{"status":200, "msg":"请求成功", "data":{"豌豆荚":989,"vivo":2,"360":6}}'}]
			"""