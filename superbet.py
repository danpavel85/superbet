import scrapy
import json
from scrapy.http.request import Request
from datetime import datetime

class SuperbetSpider(scrapy.Spider):
	name = 'superbet'
	allowed_domains = ['superbet.ro']
	current_date  = datetime.today().strftime('%Y-%m-%d')
	current_time = '00:00:01'
	current_date_time = current_date + '+' + current_time
	url = 'https://offer1.superbet.ro/offer/getOfferByDate?compression=true&langId=2&controller=offer&method=getOfferByDate&preselected=true&offerState=prematch&startDate={}&endDate='
	start_urls = [url.format(current_date_time)]
	
	def parse(self, response):
		jsonresponse = json.loads(response.body_as_unicode())
		all_matches = jsonresponse.get('data')
		for x in all_matches:
			if x['si'] == 5:
				match_id = x['mi']

				relative_url = 'https://offer1.superbet.ro/matches/getMatchesByIds?compression=true&langId=2&controller=matches&method=getMatchesByIds&matchIds={}'
				complete_url = relative_url.format(match_id)

				yield Request(complete_url, callback=self.parse_odds)

	def parse_odds(self, response):
		jsonresponse = json.loads(response.body_as_unicode())
		matches = jsonresponse.get('data')
		for x in matches:
			try:
				nm = []
				name = x['mn']
				nm.append(name)
				home, away = zip(*(s.split("·") for s in nm))
				home = str(home).replace("('", '')
				home = home.replace("',)", '')
				away = str(away).replace("('", '')
				away = away.replace("',)", '')
			except:
				pass
			
			try:
				league = x["tn2"]
				league = league.split('|', 1)[0]
				cl = []
				league = league.replace(' - ', '#')
				cl.append(league)
				country = None
				country, league =  zip(*(s.split("#") for s in cl))
				country = str(country).replace("('", '')
				country = country.replace("',)", '')
				league = str(league).replace("('", '')
				league = league.replace("',)", '')
			except:
				pass
			dt = x["mld"]
			s_id = x["_id"]
			odds = x['odds']
			
			_1_= None
			for _1__odds in odds:
				if _1__odds['oc'] == "11":
					_1_ = _1__odds['ov']
			_X_= None
			for _X__odds in odds:
				if _X__odds['oc'] == "10":
					_X_ = _X__odds['ov']
			_2_= None
			for _2__odds in odds:
				if _2__odds['oc'] == "12":
					_2_ = _2__odds['ov']
			_1X_ = None
			for _1X__odds in odds:
				if _1X__odds['oc'] == "110":
					_1X_ = _1X__odds['ov']
			_X2_ = None
			for _X2__odds in odds:
				if _X2__odds['oc'] == "102":
					_X2_ = _X2__odds['ov']
			_12_ = None
			for _12__odds in odds:
				if _12__odds['oc'] == "112":
					_12_ = _12__odds['ov']
			_1_1_ = None
			for _1_1__odds in odds:
				if _1_1__odds['oc'] == "611":
					_1_1_ = _1_1__odds['ov']
			_1_X_ = None
			for _1_X__odds in odds:
				if _1_X__odds['oc'] == "610":
					_1_X_ = _1_X__odds['ov']
			_1_2_ = None
			for _1_2__odds in odds:
				if _1_2__odds['oc'] == "612":
					_1_2_ = _1_2__odds['ov']
			_X_1_ = None
			for _X_1__odds in odds:
				if _X_1__odds['oc'] == "601":
					_X_1_ = _X_1__odds['ov']
			_X_X_ = None
			for _X_X__odds in odds:
				if _X_X__odds['oc'] == "600":
					_X_X_ = _X_X__odds['ov']
			_X_2_ = None
			for _X_2__odds in odds:
				if _X_2__odds['oc'] == "602":
					_X_2_ = _X_2__odds['ov']
			_2_1_ = None
			for _2_1__odds in odds:
				if _2_1__odds['oc'] == "621":
					_2_1_ = _2_1__odds['ov']
			_2_X_ = None
			for _2_X__odds in odds:
				if _2_X__odds['oc'] == "620":
					_2_X_ = _2_X__odds['ov']
			_2_2_ = None
			for _2_2__odds in odds:
				if _2_2__odds['oc'] == "622":
					_2_2_ = _2_2__odds['ov']
			_1_1X_ = None
			for _1_1X__odds in odds:
				if _1_1X__odds['oc'] == "655":
					_1_1X_ = _1_1X__odds['ov']
			_1_X2_ = None
			for _1_X2__odds in odds:
				if _1_X2__odds['oc'] == "656":
					_1_X2_ = _1_X2__odds['ov']
			_1_12_ = None
			for _1_12__odds in odds:
				if _1_12__odds['oc'] == "660":
					_1_12_ = _1_12__odds['ov']
			_X_1X_ = None
			for _X_1X__odds in odds:
				if _X_1X__odds['oc'] == "661":
					_X_1X_ = _X_1X__odds['ov']
			_X_X2_ = None
			for _X_X2__odds in odds:
				if _X_X2__odds['oc'] == "662":
					_X_X2_ = _X_X2__odds['ov']
			_X_12_ = None
			for _X_12__odds in odds:
				if _X_12__odds['oc'] == "663":
					_X_12_ = _X_12__odds['ov']
			_2_1X_ = None
			for _2_1X__odds in odds:
				if _2_1X__odds['oc'] == "664":
					_2_1X_ = _2_1X__odds['ov']
			_2_X2_ = None
			for _2_X2__odds in odds:
				if _2_X2__odds['oc'] == "665":
					_2_X2_ = _2_X2__odds['ov']
			_2_12_ = None
			for _2_12__odds in odds:
				if _2_12__odds['oc'] == "700":
					_2_12_ = _2_12__odds['ov']
			_1X_1_ = None
			for _1X_1__odds in odds:
				if _1X_1__odds['oc'] == "39":
					_1X_1_ = _1X_1__odds['ov']
			_1X_X_ = None
			for _1X_X__odds in odds:
				if _1X_X__odds['oc'] == "701":
					_1X_X_ = _1X_X__odds['ov']
			_1X_2_ = None
			for _1X_2__odds in odds:
				if _1X_2__odds['oc'] == "702":
					_1X_2_ = _1X_2__odds['ov']
			_X2_1_ = None
			for _X2_1__odds in odds:
				if _X2_1__odds['oc'] == "703":
					_X2_1_ = _X2_1__odds['ov']
			_X2_X_ = None
			for _X2_X__odds in odds:
				if _X2_X__odds['oc'] == "704":
					_X2_X_ = _X2_X__odds['ov']
			_X2_2_ = None
			for _X2_2__odds in odds:
				if _X2_2__odds['oc'] == "40":
					_X2_2_ = _X2_2__odds['ov']
			_12_1_ = None
			for _12_1__odds in odds:
				if _12_1__odds['oc'] == "705":
					_12_1_ = _12_1__odds['ov']
			_12_X_ = None
			for _12_X__odds in odds:
				if _12_X__odds['oc'] == "706":
					_12_X_ = _12_X__odds['ov']
			_12_2_ = None
			for _12_2__odds in odds:
				if _12_2__odds['oc'] == "712":
					_12_2_ = _12_2__odds['ov']
			_NUX_2_ = None
			for _NUX_2__odds in odds:
				if _NUX_2__odds['oc'] == "49":
					_NUX_2_ = _NUX_2__odds['ov']
			_NUX_X_ = None
			for _NUX_X__odds in odds:
				if _NUX_X__odds['oc'] == "53":
					_NUX_X_ = _NUX_X__odds['ov']
			_NU1_1_ = None
			for _NU1_1__odds in odds:
				if _NU1_1__odds['oc'] == "46":
					_NU1_1_ = _NU1_1__odds['ov']
			_1X_1X_ = None
			for _1X_1X__odds in odds:
				if _1X_1X__odds['oc'] == "151":
					_1X_1X_ = _1X_1X__odds['ov']
			_1X_12_ = None
			for _1X_12__odds in odds:
				if _1X_12__odds['oc'] == "721":
					_1X_12_ = _1X_12__odds['ov']
			_X2_X2_ = None
			for _X2_X2__odds in odds:
				if _X2_X2__odds['oc'] == "152":
					_X2_X2_ = _X2_X2__odds['ov']
			_X2_12_ = None
			for _X2_12__odds in odds:
				if _X2_12__odds['oc'] == "730":
					_X2_12_ = _X2_12__odds['ov']
			_12_12_ = None
			for _12_12__odds in odds:
				if _12_12__odds['oc'] == "45":
					_12_12_ = _12_12__odds['ov']
			_X2_1X_ = None
			for _X2_1X__odds in odds:
				if _X2_1X__odds['oc'] == "44":
					_X2_1X_ = _X2_1X__odds['ov']
			_1X_X2_ = None
			for _1X_X2__odds in odds:
				if _1X_X2__odds['oc'] == "43":
					_1X_X2_ = _1X_X2__odds['ov']
			_12_1X_ = None
			for _12_1X__odds in odds:
				if _12_1X__odds['oc'] == "733":
					_12_1X_ = _12_1X__odds['ov']
			_12_X2_ = None
			for _12_X2__odds in odds:
				if _12_X2__odds['oc'] == "745":
					_12_X2_ = _12_X2__odds['ov']
			_NU2_2_ = None
			for _NU2_2__odds in odds:
				if _NU2_2__odds['oc'] == "47":
					_NU2_2_ = _NU2_2__odds['ov']
			_NUX_1_ = None
			for _NUX_1__odds in odds:
				if _NUX_1__odds['oc'] == "48":
					_NUX_1_ = _NUX_1__odds['ov']
			_I1_ = None
			for _I1__odds in odds:
				if _I1__odds['oc'] == "21":
					_I1_ = _I1__odds['ov']
			_IX_ = None
			for _IX__odds in odds:
				if _IX__odds['oc'] == "20":
					_IX_ = _IX__odds['ov']
			_I2_ = None
			for _I2__odds in odds:
				if _I2__odds['oc'] == "22":
					_I2_ = _I2__odds['ov']
			_I1X_ = None
			for _I1X__odds in odds:
				if _I1X__odds['oc'] == "210":
					_I1X_ = _I1X__odds['ov']
			_IX2_ = None
			for _IX2__odds in odds:
				if _IX2__odds['oc'] == "202":
					_IX2_ = _IX2__odds['ov']
			_I12_ = None
			for _I12__odds in odds:
				if _I12__odds['oc'] == "212":
					_I12_ = _I12__odds['ov']
			_II1_ = None
			for _II1__odds in odds:
				if _II1__odds['oc'] == "31":
					_II1_ = _II1__odds['ov']
			_IIX_ = None
			for _IIX__odds in odds:
				if _IIX__odds['oc'] == "30":
					_IIX_ = _IIX__odds['ov']
			_II2_ = None
			for _II2__odds in odds:
				if _II2__odds['oc'] == "32":
					_II2_ = _II2__odds['ov']
			_II1X_ = None
			for _II1X__odds in odds:
				if _II1X__odds['oc'] == "310":
					_II1X_ = _II1X__odds['ov']
			_IIX2_ = None
			for _IIX2__odds in odds:
				if _IIX2__odds['oc'] == "302":
					_IIX2_ = _IIX2__odds['ov']
			_II12_ = None
			for _II12__odds in odds:
				if _II12__odds['oc'] == "312":
					_II12_ = _II12__odds['ov']
			_PsF1_ = None
			for _PsF1__odds in odds:
				if _PsF1__odds['oc'] == "51":
					_PsF1_ = _PsF1__odds['ov']
			_PsFX_ = None
			for _PsFX__odds in odds:
				if _PsFX__odds['oc'] == "50":
					_PsFX_ = _PsFX__odds['ov']
			_PsF2_ = None
			for _PsF2__odds in odds:
				if _PsF2__odds['oc'] == "52":
					_PsF2_ = _PsF2__odds['ov']
			_H1_1pt5_ = None
			for _H1_1pt5__odds in odds:
				if _H1_1pt5__odds['oc'] == "41":
					_H1_1pt5_ = _H1_1pt5__odds['ov']
			_H2_1pt5_ = None
			for _H2_1pt5__odds in odds:
				if _H2_1pt5__odds['oc'] == "42":
					_H2_1pt5_ = _H2_1pt5__odds['ov']
			_DNB1_ = None
			for _DNB1__odds in odds:
				if _DNB1__odds['oc'] == "81":
					_DNB1_ = _DNB1__odds['ov']
			_IDNB1_ = None
			for _IDNB1__odds in odds:
				if _IDNB1__odds['oc'] == "83":
					_IDNB1_ = _IDNB1__odds['ov']
			_DNB2_ = None
			for _DNB2__odds in odds:
				if _DNB2__odds['oc'] == "82":
					_DNB2_ = _DNB2__odds['ov']
			_IDNB2_ = None
			for _IDNB2__odds in odds:
				if _IDNB2__odds['oc'] == "84":
					_IDNB2_ = _IDNB2__odds['ov']
			_0_1_ = None
			for _0_1__odds in odds:
				if _0_1__odds['oc'] == "0-1":
					_0_1_ = _0_1__odds['ov']
			_0_2_ = None
			for _0_2__odds in odds:
				if _0_2__odds['oc'] == "0-2":
					_0_2_ = _0_2__odds['ov']
			_0_3_ = None
			for _0_3__odds in odds:
				if _0_3__odds['oc'] == "0-3":
					_0_3_ = _0_3__odds['ov']
			_0_4_ = None
			for _0_4__odds in odds:
				if _0_4__odds['oc'] == "0-4":
					_0_4_ = _0_4__odds['ov']
			_0_5_ = None
			for _0_5__odds in odds:
				if _0_5__odds['oc'] == "0-5":
					_0_5_ = _0_5__odds['ov']
			_1__2_ = None
			for _1__2__odds in odds:
				if _1__2__odds['oc'] == "1-2":
					_1__2_ = _1__2__odds['ov']
			_1_3_ = None
			for _1_3__odds in odds:
				if _1_3__odds['oc'] == "1-3":
					_1_3_ = _1_3__odds['ov']
			_1_4_ = None
			for _1_4__odds in odds:
				if _1_4__odds['oc'] == "1-4":
					_1_4_ = _1_4__odds['ov']
			_1_5_ = None
			for _1_5__odds in odds:
				if _1_5__odds['oc'] == "1-5":
					_1_5_ = _1_5__odds['ov']
			_1_6_ = None
			for _1_6__odds in odds:
				if _1_6__odds['oc'] == "1-6":
					_1_6_ = _1_6__odds['ov']
			_2_3_ = None
			for _2_3__odds in odds:
				if _2_3__odds['oc'] == "2-3":
					_2_3_ = _2_3__odds['ov']
			_2_4_ = None
			for _2_4__odds in odds:
				if _2_4__odds['oc'] == "2-4":
					_2_4_ = _2_4__odds['ov']
			_2_5_ = None
			for _2_5__odds in odds:
				if _2_5__odds['oc'] == "2-5":
					_2_5_ = _2_5__odds['ov']
			_2_6_ = None
			for _2_6__odds in odds:
				if _2_6__odds['oc'] == "2-6":
					_2_6_ = _2_6__odds['ov']
			_3_4_ = None
			for _3_4__odds in odds:
				if _3_4__odds['oc'] == "3-4":
					_3_4_ = _3_4__odds['ov']
			_3_5_ = None
			for _3_5__odds in odds:
				if _3_5__odds['oc'] == "3-5":
					_3_5_ = _3_5__odds['ov']
			_3_6_ = None
			for _3_6__odds in odds:
				if _3_6__odds['oc'] == "3-6":
					_3_6_ = _3_6__odds['ov']
			_4_5_ = None
			for _4_5__odds in odds:
				if _4_5__odds['oc'] == "4-5":
					_4_5_ = _4_5__odds['ov']
			_4_6_ = None
			for _4_6__odds in odds:
				if _4_6__odds['oc'] == "4-6":
					_4_6_ = _4_6__odds['ov']
			_1p_ = None
			for _1p__odds in odds:
				if _1p__odds['oc'] == "1+":
					_1p_ = _1p__odds['ov']
			_2p_ = None
			for _2p__odds in odds:
				if _2p__odds['oc'] == "2+":
					_2p_ = _2p__odds['ov']
			_3p_ = None
			for _3p__odds in odds:
				if _3p__odds['oc'] == "3+":
					_3p_ = _3p__odds['ov']
			_4p_ = None
			for _4p__odds in odds:
				if _4p__odds['oc'] == "4+":
					_4p_ = _4p__odds['ov']
			_5p_ = None
			for _5p__odds in odds:
				if _5p__odds['oc'] == "5+":
					_5p_ = _5p__odds['ov']
			_6p_ = None
			for _6p__odds in odds:
				if _6p__odds['oc'] == "6+":
					_6p_ = _6p__odds['ov']
			_7p_ = None
			for _7p__odds in odds:
				if _7p__odds['oc'] == "7+":
					_7p_ = _7p__odds['ov']
			_E2_ = None
			for _E2__odds in odds:
				if _E2__odds['oc'] == "+2":
					_E2_ = _E2__odds['ov']
			_E3_ = None
			for _E3__odds in odds:
				if _E3__odds['oc'] == "+3":
					_E3_ = _E3__odds['ov']
			_E4_ = None
			for _E4__odds in odds:
				if _E4__odds['oc'] == "+4":
					_E4_ = _E4__odds['ov']
			_NE2_ = None
			for _NE2__odds in odds:
				if _NE2__odds['oc'] == "-2":
					_NE2_ = _NE2__odds['ov']
			_NE3_ = None
			for _NE3__odds in odds:
				if _NE3__odds['oc'] == "-3":
					_NE3_ = _NE3__odds['ov']
			_NE4_ = None
			for _NE4__odds in odds:
				if _NE4__odds['oc'] == "-4":
					_NE4_ = _NE4__odds['ov']
			_NE1_ = None
			for _NE1__odds in odds:
				if _NE1__odds['oc'] == "-1":
					_NE1_ = _NE1__odds['ov']
			_I0_1_ = None
			for _I0_1__odds in odds:
				if _I0_1__odds['oc'] == "101":
					_I0_1_ = _I0_1__odds['ov']
			_I0_2_ = None
			for _I0_2__odds in odds:
				if _I0_2__odds['oc'] == "1021":
					_I0_2_ = _I0_2__odds['ov']
			_I1_2_ = None
			for _I1_2__odds in odds:
				if _I1_2__odds['oc'] == "1121":
					_I1_2_ = _I1_2__odds['ov']
			_I1_3_ = None
			for _I1_3__odds in odds:
				if _I1_3__odds['oc'] == "1131":
					_I1_3_ = _I1_3__odds['ov']
			_I2_3_ = None
			for _I2_3__odds in odds:
				if _I2_3__odds['oc'] == "123":
					_I2_3_ = _I2_3__odds['ov']
			_I1p_ = None
			for _I1p__odds in odds:
				if _I1p__odds['oc'] == "11+":
					_I1p_ = _I1p__odds['ov']
			_I2p_ = None
			for _I2p__odds in odds:
				if _I2p__odds['oc'] == "12+":
					_I2p_ = _I2p__odds['ov']
			_I3p_ = None
			for _I3p__odds in odds:
				if _I3p__odds['oc'] == "13+":
					_I3p_ = _I3p__odds['ov']
			_I4p_ = None
			for _I4p__odds in odds:
				if _I4p__odds['oc'] == "14+":
					_I4p_ = _I4p__odds['ov']
			_IE1_ = None
			for _IE1__odds in odds:
				if _IE1__odds['oc'] == "54":
					_IE1_ = _IE1__odds['ov']
			_IE2_ = None
			for _IE2__odds in odds:
				if _IE2__odds['oc'] == "55":
					_IE2_ = _IE2__odds['ov']
			_INE1_ = None
			for _INE1__odds in odds:
				if _INE1__odds['oc'] == "56":
					_INE1_ = _INE1__odds['ov']
			_INE2_ = None
			for _INE2__odds in odds:
				if _INE2__odds['oc'] == "57":
					_INE2_ = _INE2__odds['ov']
			_II0_1_ = None
			for _II0_1__odds in odds:
				if _II0_1__odds['oc'] == "201":
					_II0_1_ = _II0_1__odds['ov']
			_II0_3_ = None
			for _II0_3__odds in odds:
				if _II0_3__odds['oc'] == "2032":
					_II0_3_ = _II0_3__odds['ov']
			_II0_2_ = None
			for _II0_2__odds in odds:
				if _II0_2__odds['oc'] == "2022":
					_II0_2_ = _II0_2__odds['ov']
			_II1_2_ = None
			for _II1_2__odds in odds:
				if _II1_2__odds['oc'] == "2122":
					_II1_2_ = _II1_2__odds['ov']
			_II1_3_ = None
			for _II1_3__odds in odds:
				if _II1_3__odds['oc'] == "2132":
					_II1_3_ = _II1_3__odds['ov']
			_II2_3_ = None
			for _II2_3__odds in odds:
				if _II2_3__odds['oc'] == "223":
					_II2_3_ = _II2_3__odds['ov']
			_II1p_ = None
			for _II1p__odds in odds:
				if _II1p__odds['oc'] == "21+":
					_II1p_ = _II1p__odds['ov']
			_II2p_ = None
			for _II2p__odds in odds:
				if _II2p__odds['oc'] == "22+":
					_II2p_ = _II2p__odds['ov']
			_II3p_ = None
			for _II3p__odds in odds:
				if _II3p__odds['oc'] == "23+":
					_II3p_ = _II3p__odds['ov']
			_II4p_ = None
			for _II4p__odds in odds:
				if _II4p__odds['oc'] == "24+":
					_II4p_ = _II4p__odds['ov']
			_IIE1_ = None
			for _IIE1__odds in odds:
				if _IIE1__odds['oc'] == "58":
					_IIE1_ = _IIE1__odds['ov']
			_IIE2_ = None
			for _IIE2__odds in odds:
				if _IIE2__odds['oc'] == "59":
					_IIE2_ = _IIE2__odds['ov']
			_IINE1_ = None
			for _IINE1__odds in odds:
				if _IINE1__odds['oc'] == "63":
					_IINE1_ = _IINE1__odds['ov']
			_IINE2_ = None
			for _IINE2__odds in odds:
				if _IINE2__odds['oc'] == "64":
					_IINE2_ = _IINE2__odds['ov']
			_INGG_ = None
			for _INGG__odds in odds:
				if _INGG__odds['oc'] == "7410":
					_INGG_ = _INGG__odds['ov']
			_NGG4p_ = None
			for _NGG4p__odds in odds:
				if _NGG4p__odds['oc'] == "236":
					_NGG4p_ = _NGG4p__odds['ov']
			_IINGG_ = None
			for _IINGG__odds in odds:
				if _IINGG__odds['oc'] == "7420":
					_IINGG_ = _IINGG__odds['ov']
			_INGGsiIINGG_ = None
			for _INGGsiIINGG__odds in odds:
				if _INGGsiIINGG__odds['oc'] == "251":
					_INGGsiIINGG_ = _INGGsiIINGG__odds['ov']
			_NGG3p_ = None
			for _NGG3p__odds in odds:
				if _NGG3p__odds['oc'] == "7130":
					_NGG3p_ = _NGG3p__odds['ov']
			_GG_ = None
			for _GG__odds in odds:
				if _GG__odds['oc'] == "711":
					_GG_ = _GG__odds['ov']
			_GGsi2_4_ = None
			for _GGsi2_4__odds in odds:
				if _GGsi2_4__odds['oc'] == "243":
					_GGsi2_4_ = _GGsi2_4__odds['ov']
			_NGG_ = None
			for _NGG__odds in odds:
				if _NGG__odds['oc'] == "722":
					_NGG_ = _NGG__odds['ov']
			_GG3p_ = None
			for _GG3p__odds in odds:
				if _GG3p__odds['oc'] == "713":
					_GG3p_ = _GG3p__odds['ov']
			_GGsi3_6_ = None
			for _GGsi3_6__odds in odds:
				if _GGsi3_6__odds['oc'] == "245":
					_GGsi3_6_ = _GGsi3_6__odds['ov']
			_GGsi3_5_ = None
			for _GGsi3_5__odds in odds:
				if _GGsi3_5__odds['oc'] == "244":
					_GGsi3_5_ = _GGsi3_5__odds['ov']
			_GGsi2_3_ = None
			for _GGsi2_3__odds in odds:
				if _GGsi2_3__odds['oc'] == "242":
					_GGsi2_3_ = _GGsi2_3__odds['ov']
			_GGsiG2p_ = None
			for _GGsiG2p__odds in odds:
				if _GGsiG2p__odds['oc'] == "240":
					_GGsiG2p_ = _GGsiG2p__odds['ov']
			_IIGG_ = None
			for _IIGG__odds in odds:
				if _IIGG__odds['oc'] == "742":
					_IIGG_ = _IIGG__odds['ov']
			_GGsiO2p_ = None
			for _GGsiO2p__odds in odds:
				if _GGsiO2p__odds['oc'] == "241":
					_GGsiO2p_ = _GGsiO2p__odds['ov']
			_GG4p_ = None
			for _GG4p__odds in odds:
				if _GG4p__odds['oc'] == "714":
					_GG4p_ = _GG4p__odds['ov']
			_INGGsiIIGG_ = None
			for _INGGsiIIGG__odds in odds:
				if _INGGsiIIGG__odds['oc'] == "250":
					_INGGsiIIGG_ = _INGGsiIIGG__odds['ov']
			_IGG_ = None
			for _IGG__odds in odds:
				if _IGG__odds['oc'] == "741":
					_IGG_ = _IGG__odds['ov']
			_IGGsiIINGG_ = None
			for _IGGsiIINGG__odds in odds:
				if _IGGsiIINGG__odds['oc'] == "246":
					_IGGsiIINGG_ = _IGGsiIINGG__odds['ov']
			_G2pO2p_ = None
			for _G2pO2p__odds in odds:
				if _G2pO2p__odds['oc'] == "719":
					_G2pO2p_ = _G2pO2p__odds['ov']
			_IGGsiIIGG_ = None
			for _IGGsiIIGG__odds in odds:
				if _IGGsiIIGG__odds['oc'] == "744":
					_IGGsiIIGG_ = _IGGsiIIGG__odds['ov']
			_I0_3siII0_3_ = None
			for _I0_3siII0_3__odds in odds:
				if _I0_3siII0_3__odds['oc'] == "743":
					_I0_3siII0_3_ = _I0_3siII0_3__odds['ov']
			_I0_2siII0_3_ = None
			for _I0_2siII0_3__odds in odds:
				if _I0_2siII0_3__odds['oc'] == "76":
					_I0_2siII0_3_ = _I0_2siII0_3__odds['ov']
			_I0_3siII0_2_ = None
			for _I0_3siII0_2__odds in odds:
				if _I0_3siII0_2__odds['oc'] == "78":
					_I0_3siII0_2_ = _I0_3siII0_2__odds['ov']
			_I0_2siII0_2_ = None
			for _I0_2siII0_2__odds in odds:
				if _I0_2siII0_2__odds['oc'] == "75":
					_I0_2siII0_2_ = _I0_2siII0_2__odds['ov']
			_I0_1siII0_3_ = None
			for _I0_1siII0_3__odds in odds:
				if _I0_1siII0_3__odds['oc'] == "73":
					_I0_1siII0_3_ = _I0_1siII0_3__odds['ov']
			_I1psi2p_ = None
			for _I1psi2p__odds in odds:
				if _I1psi2p__odds['oc'] == "79":
					_I1psi2p_ = _I1psi2p__odds['ov']
			_I0_1siII0_2_ = None
			for _I0_1siII0_2__odds in odds:
				if _I0_1siII0_2__odds['oc'] == "0102":
					_I0_1siII0_2_ = _I0_1siII0_2__odds['ov']
			_I0_3siII0_1_ = None
			for _I0_3siII0_1__odds in odds:
				if _I0_3siII0_1__odds['oc'] == "77":
					_I0_3siII0_1_ = _I0_3siII0_1__odds['ov']
			_I0_2siII0_1_ = None
			for _I0_2siII0_1__odds in odds:
				if _I0_2siII0_1__odds['oc'] == "74":
					_I0_2siII0_1_ = _I0_2siII0_1__odds['ov']
			_I1psiII1p_ = None
			for _I1psiII1p__odds in odds:
				if _I1psiII1p__odds['oc'] == "923":
					_I1psiII1p_ = _I1psiII1p__odds['ov']
			_I0_1siII0_1_ = None
			for _I0_1siII0_1__odds in odds:
				if _I0_1siII0_1__odds['oc'] == "0101":
					_I0_1siII0_1_ = _I0_1siII0_1__odds['ov']
			_I1psi3p_ = None
			for _I1psi3p__odds in odds:
				if _I1psi3p__odds['oc'] == "80":
					_I1psi3p_ = _I1psi3p__odds['ov']
			_I1psiII2p_ = None
			for _I1psiII2p__odds in odds:
				if _I1psiII2p__odds['oc'] == "922":
					_I1psiII2p_ = _I1psiII2p__odds['ov']
			_I2psi3p_ = None
			for _I2psi3p__odds in odds:
				if _I2psi3p__odds['oc'] == "100":
					_I2psi3p_ = _I2psi3p__odds['ov']
			_I2psiII1p_ = None
			for _I2psiII1p__odds in odds:
				if _I2psiII1p__odds['oc'] == "921":
					_I2psiII1p_ = _I2psiII1p__odds['ov']
			_I1psi4p_ = None
			for _I1psi4p__odds in odds:
				if _I1psi4p__odds['oc'] == "87":
					_I1psi4p_ = _I1psi4p__odds['ov']
			_I2psi4p_ = None
			for _I2psi4p__odds in odds:
				if _I2psi4p__odds['oc'] == "103":
					_I2psi4p_ = _I2psi4p__odds['ov']
			_I2psiII2p_ = None
			for _I2psiII2p__odds in odds:
				if _I2psiII2p__odds['oc'] == "66":
					_I2psiII2p_ = _I2psiII2p__odds['ov']
			_I1psiII3p_ = None
			for _I1psiII3p__odds in odds:
				if _I1psiII3p__odds['oc'] == "65":
					_I1psiII3p_ = _I1psiII3p__odds['ov']
			_I3psiII1p_ = None
			for _I3psiII1p__odds in odds:
				if _I3psiII1p__odds['oc'] == "68":
					_I3psiII1p_ = _I3psiII1p__odds['ov']
			_I2psi5p_ = None
			for _I2psi5p__odds in odds:
				if _I2psi5p__odds['oc'] == "104":
					_I2psi5p_ = _I2psi5p__odds['ov']
			_I2psiII3p_ = None
			for _I2psiII3p__odds in odds:
				if _I2psiII3p__odds['oc'] == "67":
					_I2psiII3p_ = _I2psiII3p__odds['ov']
			_I3psiII2p_ = None
			for _I3psiII2p__odds in odds:
				if _I3psiII2p__odds['oc'] == "69":
					_I3psiII2p_ = _I3psiII2p__odds['ov']
			_I3psiII3p_ = None
			for _I3psiII3p__odds in odds:
				if _I3psiII3p__odds['oc'] == "70":
					_I3psiII3p_ = _I3psiII3p__odds['ov']
			_PGG_ = None
			for _PGG__odds in odds:
				if _PGG__odds['oc'] == "01":
					_PGG_ = _PGG__odds['ov']
			_PGO_ = None
			for _PGO__odds in odds:
				if _PGO__odds['oc'] == "02":
					_PGO_ = _PGO__odds['ov']
			_G0_2_ = None
			for _G0_2__odds in odds:
				if _G0_2__odds['oc'] == "106":
					_G0_2_ = _G0_2__odds['ov']
			_GNE2_ = None
			for _GNE2__odds in odds:
				if _GNE2__odds['oc'] == "127":
					_GNE2_ = _GNE2__odds['ov']
			_G1p_ = None
			for _G1p__odds in odds:
				if _G1p__odds['oc'] == "71":
					_G1p_ = _G1p__odds['ov']
			_G1_3_ = None
			for _G1_3__odds in odds:
				if _G1_3__odds['oc'] == "114":
					_G1_3_ = _G1_3__odds['ov']
			_GNE1_ = None
			for _GNE1__odds in odds:
				if _GNE1__odds['oc'] == "125":
					_GNE1_ = _GNE1__odds['ov']
			_G0_1_ = None
			for _G0_1__odds in odds:
				if _G0_1__odds['oc'] == "7160":
					_G0_1_ = _G0_1__odds['ov']
			_G1_2_ = None
			for _G1_2__odds in odds:
				if _G1_2__odds['oc'] == "113":
					_G1_2_ = _G1_2__odds['ov']
			_G2p_ = None
			for _G2p__odds in odds:
				if _G2p__odds['oc'] == "716":
					_G2p_ = _G2p__odds['ov']
			_GE1_ = None
			for _GE1__odds in odds:
				if _GE1__odds['oc'] == "116":
					_GE1_ = _GE1__odds['ov']
			_G2_3_ = None
			for _G2_3__odds in odds:
				if _G2_3__odds['oc'] == "115":
					_G2_3_ = _G2_3__odds['ov']
			_GNG_ = None
			for _GNG__odds in odds:
				if _GNG__odds['oc'] == "710":
					_GNG_ = _GNG__odds['ov']
			_GE2_ = None
			for _GE2__odds in odds:
				if _GE2__odds['oc'] == "124":
					_GE2_ = _GE2__odds['ov']
			_G3p_ = None
			for _G3p__odds in odds:
				if _G3p__odds['oc'] == "723":
					_G3p_ = _G3p__odds['ov']
			_G4p_ = None
			for _G4p__odds in odds:
				if _G4p__odds['oc'] == "105":
					_G4p_ = _G4p__odds['ov']
			_O0_2_ = None
			for _O0_2__odds in odds:
				if _O0_2__odds['oc'] == "126":
					_O0_2_ = _O0_2__odds['ov']
			_ONE2_ = None
			for _ONE2__odds in odds:
				if _ONE2__odds['oc'] == "156":
					_ONE2_ = _ONE2__odds['ov']
			_O0_1_ = None
			for _O0_1__odds in odds:
				if _O0_1__odds['oc'] == "7260":
					_O0_1_ = _O0_1__odds['ov']
			_O1p_ = None
			for _O1p__odds in odds:
				if _O1p__odds['oc'] == "72":
					_O1p_ = _O1p__odds['ov']
			_O1_3_ = None
			for _O1_3__odds in odds:
				if _O1_3__odds['oc'] == "142":
					_O1_3_ = _O1_3__odds['ov']
			_ONE1_ = None
			for _ONE1__odds in odds:
				if _ONE1__odds['oc'] == "155":
					_ONE1_ = _ONE1__odds['ov']
			_O1_2_ = None
			for _O1_2__odds in odds:
				if _O1_2__odds['oc'] == "141":
					_O1_2_ = _O1_2__odds['ov']
			_OE1_ = None
			for _OE1__odds in odds:
				if _OE1__odds['oc'] == "153":
					_OE1_ = _OE1__odds['ov']
			_ONG_ = None
			for _ONG__odds in odds:
				if _ONG__odds['oc'] == "720":
					_ONG_ = _ONG__odds['ov']
			_O2p_ = None
			for _O2p__odds in odds:
				if _O2p__odds['oc'] == "726":
					_O2p_ = _O2p__odds['ov']
			_O2_3_ = None
			for _O2_3__odds in odds:
				if _O2_3__odds['oc'] == "150":
					_O2_3_ = _O2_3__odds['ov']
			_OE2_ = None
			for _OE2__odds in odds:
				if _OE2__odds['oc'] == "154":
					_OE2_ = _OE2__odds['ov']
			_O3p_ = None
			for _O3p__odds in odds:
				if _O3p__odds['oc'] == "724":
					_O3p_ = _O3p__odds['ov']
			_O4p_ = None
			for _O4p__odds in odds:
				if _O4p__odds['oc'] == "4242":
					_O4p_ = _O4p__odds['ov']
			_O0_3_ = None
			for _O0_3__odds in odds:
				if _O0_3__odds['oc'] == "130":
					_O0_3_ = _O0_3__odds['ov']
			_IG0_1_ = None
			for _IG0_1__odds in odds:
				if _IG0_1__odds['oc'] == "161":
					_IG0_1_ = _IG0_1__odds['ov']
			_IGNG_ = None
			for _IGNG__odds in odds:
				if _IGNG__odds['oc'] == "7510":
					_IGNG_ = _IGNG__odds['ov']
			_IG1p_ = None
			for _IG1p__odds in odds:
				if _IG1p__odds['oc'] == "751":
					_IG1p_ = _IG1p__odds['ov']
			_IG1_2_ = None
			for _IG1_2__odds in odds:
				if _IG1_2__odds['oc'] == "162":
					_IG1_2_ = _IG1_2__odds['ov']
			_IG2p_ = None
			for _IG2p__odds in odds:
				if _IG2p__odds['oc'] == "753":
					_IG2p_ = _IG2p__odds['ov']
			_IG3p_ = None
			for _IG3p__odds in odds:
				if _IG3p__odds['oc'] == "160":
					_IG3p_ = _IG3p__odds['ov']
			_IO0_1_ = None
			for _IO0_1__odds in odds:
				if _IO0_1__odds['oc'] == "164":
					_IO0_1_ = _IO0_1__odds['ov']
			_IONG_ = None
			for _IONG__odds in odds:
				if _IONG__odds['oc'] == "7520":
					_IONG_ = _IONG__odds['ov']
			_IO1p_ = None
			for _IO1p__odds in odds:
				if _IO1p__odds['oc'] == "752":
					_IO1p_ = _IO1p__odds['ov']
			_IO1_2_ = None
			for _IO1_2__odds in odds:
				if _IO1_2__odds['oc'] == "165":
					_IO1_2_ = _IO1_2__odds['ov']
			_IO2p_ = None
			for _IO2p__odds in odds:
				if _IO2p__odds['oc'] == "754":
					_IO2p_ = _IO2p__odds['ov']
			_IO3p_ = None
			for _IO3p__odds in odds:
				if _IO3p__odds['oc'] == "163":
					_IO3p_ = _IO3p__odds['ov']
			_IIG0_1_ = None
			for _IIG0_1__odds in odds:
				if _IIG0_1__odds['oc'] == "200":
					_IIG0_1_ = _IIG0_1__odds['ov']
			_IIG1p_ = None
			for _IIG1p__odds in odds:
				if _IIG1p__odds['oc'] == "761":
					_IIG1p_ = _IIG1p__odds['ov']
			_IIG1_2_ = None
			for _IIG1_2__odds in odds:
				if _IIG1_2__odds['oc'] == "203":
					_IIG1_2_ = _IIG1_2__odds['ov']
			_IIGNG_ = None
			for _IIGNG__odds in odds:
				if _IIGNG__odds['oc'] == "7610":
					_IIGNG_ = _IIGNG__odds['ov']
			_IIG2p_ = None
			for _IIG2p__odds in odds:
				if _IIG2p__odds['oc'] == "762":
					_IIG2p_ = _IIG2p__odds['ov']
			_IIG3p_ = None
			for _IIG3p__odds in odds:
				if _IIG3p__odds['oc'] == "166":
					_IIG3p_ = _IIG3p__odds['ov']
			_IIO0_1_ = None
			for _IIO0_1__odds in odds:
				if _IIO0_1__odds['oc'] == "205":
					_IIO0_1_ = _IIO0_1__odds['ov']
			_IIONG_ = None
			for _IIONG__odds in odds:
				if _IIONG__odds['oc'] == "7630":
					_IIONG_ = _IIONG__odds['ov']
			_IIO1p_ = None
			for _IIO1p__odds in odds:
				if _IIO1p__odds['oc'] == "763":
					_IIO1p_ = _IIO1p__odds['ov']
			_IIO1_2_ = None
			for _IIO1_2__odds in odds:
				if _IIO1_2__odds['oc'] == "206":
					_IIO1_2_ = _IIO1_2__odds['ov']
			_IIO2p_ = None
			for _IIO2p__odds in odds:
				if _IIO2p__odds['oc'] == "764":
					_IIO2p_ = _IIO2p__odds['ov']
			_IIO3p_ = None
			for _IIO3p__odds in odds:
				if _IIO3p__odds['oc'] == "204":
					_IIO3p_ = _IIO3p__odds['ov']
			_1si0_4_ = None
			for _1si0_4__odds in odds:
				if _1si0_4__odds['oc'] == "255":
					_1si0_4_ = _1si0_4__odds['ov']
			_1siII1p_ = None
			for _1siII1p__odds in odds:
				if _1siII1p__odds['oc'] == "264":
					_1siII1p_ = _1siII1p__odds['ov']
			_1si2_6_ = None
			for _1si2_6__odds in odds:
				if _1si2_6__odds['oc'] == "261":
					_1si2_6_ = _1si2_6__odds['ov']
			_1siI1p_ = None
			for _1siI1p__odds in odds:
				if _1siI1p__odds['oc'] == "263":
					_1siI1p_ = _1siI1p__odds['ov']
			_1si2_5_ = None
			for _1si2_5__odds in odds:
				if _1si2_5__odds['oc'] == "260":
					_1si2_5_ = _1si2_5__odds['ov']
			_1si0_3_ = None
			for _1si0_3__odds in odds:
				if _1si0_3__odds['oc'] == "254":
					_1si0_3_ = _1si0_3__odds['ov']
			_1si2_4_ = None
			for _1si2_4__odds in odds:
				if _1si2_4__odds['oc'] == "256":
					_1si2_4_ = _1si2_4__odds['ov']
			_1siI1psiII1p_ = None
			for _1siI1psiII1p__odds in odds:
				if _1siI1psiII1p__odds['oc'] == "306":
					_1siI1psiII1p_ = _1siI1psiII1p__odds['ov']
			_1si3p_ = None
			for _1si3p__odds in odds:
				if _1si3p__odds['oc'] == "90":
					_1si3p_ = _1si3p__odds['ov']
			_1siII2p_ = None
			for _1siII2p__odds in odds:
				if _1siII2p__odds['oc'] == "265":
					_1siII2p_ = _1siII2p__odds['ov']
			_1si0_2_ = None
			for _1si0_2__odds in odds:
				if _1si0_2__odds['oc'] == "253 ":
					_1si0_2_ = _1si0_2__odds['ov']
			_1si3_6_ = None
			for _1si3_6__odds in odds:
				if _1si3_6__odds['oc'] == "262":
					_1si3_6_ = _1si3_6__odds['ov']
			_1siImII_ = None
			for _1siImII__odds in odds:
				if _1siImII__odds['oc'] == "301":
					_1siImII_ = _1siImII__odds['ov']
			_1siGG_ = None
			for _1siGG__odds in odds:
				if _1siGG__odds['oc'] == "1711":
					_1siGG_ = _1siGG__odds['ov']
			_1si2_3_ = None
			for _1si2_3__odds in odds:
				if _1si2_3__odds['oc'] == "92":
					_1si2_3_ = _1si2_3__odds['ov']
			_1si3_5_ = None
			for _1si3_5__odds in odds:
				if _1si3_5__odds['oc'] == "131":
					_1si3_5_ = _1si3_5__odds['ov']
			_1siI2p_ = None
			for _1siI2p__odds in odds:
				if _1siI2p__odds['oc'] == "98":
					_1siI2p_ = _1siI2p__odds['ov']
			_1si4p_ = None
			for _1si4p__odds in odds:
				if _1si4p__odds['oc'] == "94":
					_1si4p_ = _1si4p__odds['ov']
			_1siImmII_ = None
			for _1siImmII__odds in odds:
				if _1siImmII__odds['oc'] == "266":
					_1siImmII_ = _1siImmII__odds['ov']
			_1siIeII_ = None
			for _1siIeII__odds in odds:
				if _1siIeII__odds['oc'] == "300":
					_1siIeII_ = _1siIeII__odds['ov']
			_1si5p_ = None
			for _1si5p__odds in odds:
				if _1si5p__odds['oc'] == "252":
					_1si5p_ = _1si5p__odds['ov']
			_1si2p_ = None
			for _1si2p__odds in odds:
				if _1si2p__odds['oc'] == "88":
					_1si2p_ = _1si2p__odds['ov']
			_1siG2p_ = None
			for _1siG2p__odds in odds:
				if _1siG2p__odds['oc'] == "305":
					_1siG2p_ = _1siG2p__odds['ov']
			_2si2p_ = None
			for _2si2p__odds in odds:
				if _2si2p__odds['oc'] == "89":
					_2si2p_ = _2si2p__odds['ov']
			_2siO2p_ = None
			for _2siO2p__odds in odds:
				if _2siO2p__odds['oc'] == "718":
					_2siO2p_ = _2siO2p__odds['ov']
			_2si0_4_ = None
			for _2si0_4__odds in odds:
				if _2si0_4__odds['oc'] == "326":
					_2si0_4_ = _2si0_4__odds['ov']
			_2siII1p_ = None
			for _2siII1p__odds in odds:
				if _2siII1p__odds['oc'] == "335":
					_2siII1p_ = _2siII1p__odds['ov']
			_2si2_6_ = None
			for _2si2_6__odds in odds:
				if _2si2_6__odds['oc'] == "332":
					_2si2_6_ = _2si2_6__odds['ov']
			_2siI1p_ = None
			for _2siI1p__odds in odds:
				if _2siI1p__odds['oc'] == "334":
					_2siI1p_ = _2siI1p__odds['ov']
			_2si0_3_ = None
			for _2si0_3__odds in odds:
				if _2si0_3__odds['oc'] == "325":
					_2si0_3_ = _2si0_3__odds['ov']
			_2si2_5_ = None
			for _2si2_5__odds in odds:
				if _2si2_5__odds['oc'] == "331":
					_2si2_5_ = _2si2_5__odds['ov']
			_2si2_4_ = None
			for _2si2_4__odds in odds:
				if _2si2_4__odds['oc'] == "330":
					_2si2_4_ = _2si2_4__odds['ov']
			_2siI1psiII1p_ = None
			for _2siI1psiII1p__odds in odds:
				if _2siI1psiII1p__odds['oc'] == "345":
					_2siI1psiII1p_ = _2siI1psiII1p__odds['ov']
			_2si3p_ = None
			for _2si3p__odds in odds:
				if _2si3p__odds['oc'] == "91":
					_2si3p_ = _2si3p__odds['ov']
			_2siII2p_ = None
			for _2siII2p__odds in odds:
				if _2siII2p__odds['oc'] == "336":
					_2siII2p_ = _2siII2p__odds['ov']
			_2si0_2_ = None
			for _2si0_2__odds in odds:
				if _2si0_2__odds['oc'] == "324":
					_2si0_2_ = _2si0_2__odds['ov']
			_2si3_6_ = None
			for _2si3_6__odds in odds:
				if _2si3_6__odds['oc'] == "333":
					_2si3_6_ = _2si3_6__odds['ov']
			_2siImII_ = None
			for _2siImII__odds in odds:
				if _2siImII__odds['oc'] == "342":
					_2siImII_ = _2siImII__odds['ov']
			_2siGG_ = None
			for _2siGG__odds in odds:
				if _2siGG__odds['oc'] == "2711":
					_2siGG_ = _2siGG__odds['ov']
			_2si2_3_ = None
			for _2si2_3__odds in odds:
				if _2si2_3__odds['oc'] == "93":
					_2si2_3_ = _2si2_3__odds['ov']
			_2si3_5_ = None
			for _2si3_5__odds in odds:
				if _2si3_5__odds['oc'] == "132":
					_2si3_5_ = _2si3_5__odds['ov']
			_2siI2p_ = None
			for _2siI2p__odds in odds:
				if _2siI2p__odds['oc'] == "99":
					_2siI2p_ = _2siI2p__odds['ov']
			_2siImmII_ = None
			for _2siImmII__odds in odds:
				if _2siImmII__odds['oc'] == "340":
					_2siImmII_ = _2siImmII__odds['ov']
			_2si4p_ = None
			for _2si4p__odds in odds:
				if _2si4p__odds['oc'] == "95":
					_2si4p_ = _2si4p__odds['ov']
			_2siIeII_ = None
			for _2siIeII__odds in odds:
				if _2siIeII__odds['oc'] == "341":
					_2siIeII_ = _2siIeII__odds['ov']
			_2si5p_ = None
			for _2si5p__odds in odds:
				if _2si5p__odds['oc'] == "323":
					_2si5p_ = _2si5p__odds['ov']
			_Xsi0_2_ = None
			for _Xsi0_2__odds in odds:
				if _Xsi0_2__odds['oc'] == "311":
					_Xsi0_2_ = _Xsi0_2__odds['ov']
			_Xsi2p_ = None
			for _Xsi2p__odds in odds:
				if _Xsi2p__odds['oc'] == "313":
					_Xsi2p_ = _Xsi2p__odds['ov']
			_Xsi2_4_ = None
			for _Xsi2_4__odds in odds:
				if _Xsi2_4__odds['oc'] == "316":
					_Xsi2_4_ = _Xsi2_4__odds['ov']
			_XsiIeII_ = None
			for _XsiIeII__odds in odds:
				if _XsiIeII__odds['oc'] == "321":
					_XsiIeII_ = _XsiIeII__odds['ov']
			_XsiImII_ = None
			for _XsiImII__odds in odds:
				if _XsiImII__odds['oc'] == "322":
					_XsiImII_ = _XsiImII__odds['ov']
			_XsiImmII_ = None
			for _XsiImmII__odds in odds:
				if _XsiImmII__odds['oc'] == "320":
					_XsiImmII_ = _XsiImmII__odds['ov']
			_Xsi4p_ = None
			for _Xsi4p__odds in odds:
				if _Xsi4p__odds['oc'] == "315":
					_Xsi4p_ = _Xsi4p__odds['ov']
			_ImmII_ = None
			for _ImmII__odds in odds:
				if _ImmII__odds['oc'] == "61":
					_ImmII_ = _ImmII__odds['ov']
			_IeII_ = None
			for _IeII__odds in odds:
				if _IeII__odds['oc'] == "60":
					_IeII_ = _IeII__odds['ov']
			_ImII_ = None
			for _ImII__odds in odds:
				if _ImII__odds['oc'] == "62":
					_ImII_ = _ImII__odds['ov']
			_ImmeII_ = None
			for _ImmeII__odds in odds:
				if _ImmeII__odds['oc'] == "6160":
					_ImmeII_ = _ImmeII__odds['ov']
			_ImeII_ = None
			for _ImeII__odds in odds:
				if _ImeII__odds['oc'] == "6260":
					_ImeII_ = _ImeII__odds['ov']
			_ImmmII_ = None
			for _ImmmII__odds in odds:
				if _ImmmII__odds['oc'] == "6162":
					_ImmmII_ = _ImmmII__odds['ov']
			_IG0_1siIIG0_2_ = None
			for _IG0_1siIIG0_2__odds in odds:
				if _IG0_1siIIG0_2__odds['oc'] == "220":
					_IG0_1siIIG0_2_ = _IG0_1siIIG0_2__odds['ov']
			_IG0_2siIIG0_1_ = None
			for _IG0_2siIIG0_1__odds in odds:
				if _IG0_2siIIG0_1__odds['oc'] == "221":
					_IG0_2siIIG0_1_ = _IG0_2siIIG0_1__odds['ov']
			_IG0_1siIIG0_1_ = None
			for _IG0_1siIIG0_1__odds in odds:
				if _IG0_1siIIG0_1__odds['oc'] == "216":
					_IG0_1siIIG0_1_ = _IG0_1siIIG0_1__odds['ov']
			_IGNGsIIGNG_ = None
			for _IGNGsIIGNG__odds in odds:
				if _IGNGsIIGNG__odds['oc'] == "7150":
					_IGNGsIIGNG_ = _IGNGsIIGNG__odds['ov']
			_IGNGsiIIG1p_ = None
			for _IGNGsiIIG1p__odds in odds:
				if _IGNGsiIIG1p__odds['oc'] == "755":
					_IGNGsiIIG1p_ = _IGNGsiIIG1p__odds['ov']
			_IG1psiIIG1p_ = None
			for _IG1psiIIG1p__odds in odds:
				if _IG1psiIIG1p__odds['oc'] == "715":
					_IG1psiIIG1p_ = _IG1psiIIG1p__odds['ov']
			_IG1psiIIGNG_ = None
			for _IG1psiIIGNG__odds in odds:
				if _IG1psiIIGNG__odds['oc'] == "765":
					_IG1psiIIGNG_ = _IG1psiIIGNG__odds['ov']
			_IGNGsiIIG2p_ = None
			for _IGNGsiIIG2p__odds in odds:
				if _IGNGsiIIG2p__odds['oc'] == "756":
					_IGNGsiIIG2p_ = _IGNGsiIIG2p__odds['ov']
			_IG1psiIIG2p_ = None
			for _IG1psiIIG2p__odds in odds:
				if _IG1psiIIG2p__odds['oc'] == "211":
					_IG1psiIIG2p_ = _IG1psiIIG2p__odds['ov']
			_IG2psiIIG1p_ = None
			for _IG2psiIIG1p__odds in odds:
				if _IG2psiIIG1p__odds['oc'] == "214":
					_IG2psiIIG1p_ = _IG2psiIIG1p__odds['ov']
			_IG2psiIIGNG_ = None
			for _IG2psiIIGNG__odds in odds:
				if _IG2psiIIGNG__odds['oc'] == "766":
					_IG2psiIIGNG_ = _IG2psiIIGNG__odds['ov']
			_IG2psiIIG2p_ = None
			for _IG2psiIIG2p__odds in odds:
				if _IG2psiIIG2p__odds['oc'] == "215":
					_IG2psiIIG2p_ = _IG2psiIIG2p__odds['ov']
			_IG1psiIIG3p_ = None
			for _IG1psiIIG3p__odds in odds:
				if _IG1psiIIG3p__odds['oc'] == "213":
					_IG1psiIIG3p_ = _IG1psiIIG3p__odds['ov']
			_IO0_1siIIO0_2_ = None
			for _IO0_1siIIO0_2__odds in odds:
				if _IO0_1siIIO0_2__odds['oc'] == "232":
					_IO0_1siIIO0_2_ = _IO0_1siIIO0_2__odds['ov']
			_IO0_2siIIO0_1_ = None
			for _IO0_2siIIO0_1__odds in odds:
				if _IO0_2siIIO0_1__odds['oc'] == "233":
					_IO0_2siIIO0_1_ = _IO0_2siIIO0_1__odds['ov']
			_IO0_1siIIO0_1_ = None
			for _IO0_1siIIO0_1__odds in odds:
				if _IO0_1siIIO0_1__odds['oc'] == "231":
					_IO0_1siIIO0_1_ = _IO0_1siIIO0_1__odds['ov']
			_IONGsIIONG_ = None
			for _IONGsIIONG__odds in odds:
				if _IONGsIIONG__odds['oc'] == "7250":
					_IONGsIIONG_ = _IONGsIIONG__odds['ov']
			_IONGsiIIO1p_ = None
			for _IONGsiIIO1p__odds in odds:
				if _IONGsiIIO1p__odds['oc'] == "770":
					_IONGsiIIO1p_ = _IONGsiIIO1p__odds['ov']
			_IO1psiIIO1p_ = None
			for _IO1psiIIO1p__odds in odds:
				if _IO1psiIIO1p__odds['oc'] == "725":
					_IO1psiIIO1p_ = _IO1psiIIO1p__odds['ov']
			_IO1psiIIONG_ = None
			for _IO1psiIIONG__odds in odds:
				if _IO1psiIIONG__odds['oc'] == "772":
					_IO1psiIIONG_ = _IO1psiIIONG__odds['ov']
			_IONGsiIIO2p_ = None
			for _IONGsiIIO2p__odds in odds:
				if _IONGsiIIO2p__odds['oc'] == "771":
					_IONGsiIIO2p_ = _IONGsiIIO2p__odds['ov']
			_IO1psiIIO2p_ = None
			for _IO1psiIIO2p__odds in odds:
				if _IO1psiIIO2p__odds['oc'] == "224":
					_IO1psiIIO2p_ = _IO1psiIIO2p__odds['ov']
			_IO2psiIIO1p_ = None
			for _IO2psiIIO1p__odds in odds:
				if _IO2psiIIO1p__odds['oc'] == "226":
					_IO2psiIIO1p_ = _IO2psiIIO1p__odds['ov']
			_IO2psiIIONG_ = None
			for _IO2psiIIONG__odds in odds:
				if _IO2psiIIONG__odds['oc'] == "773":
					_IO2psiIIONG_ = _IO2psiIIONG__odds['ov']
			_IO2psiIIO2p_ = None
			for _IO2psiIIO2p__odds in odds:
				if _IO2psiIIO2p__odds['oc'] == "230":
					_IO2psiIIO2p_ = _IO2psiIIO2p__odds['ov']
			_IO1psiIIO3p_ = None
			for _IO1psiIIO3p__odds in odds:
				if _IO1psiIIO3p__odds['oc'] == "225":
					_IO1psiIIO3p_ = _IO1psiIIO3p__odds['ov']
			_IO0_2siIIO0_2_ = None
			for _IO0_2siIIO0_2__odds in odds:
				if _IO0_2siIIO0_2__odds['oc'] == "234":
					_IO0_2siIIO0_2_ = _IO0_2siIIO0_2__odds['ov']
			_1__1_ = None
			for _1__1__odds in odds:
				if _1__1__odds['oc'] == "*11":
					_1__1_ = _1__1__odds['ov']
			_1__0_ = None
			for _1__0__odds in odds:
				if _1__0__odds['oc'] == "*10":
					_1__0_ = _1__0__odds['ov']
			_2__1_ = None
			for _2__1__odds in odds:
				if _2__1__odds['oc'] == "*21":
					_2__1_ = _2__1__odds['ov']
			_0__1_ = None
			for _0__1__odds in odds:
				if _0__1__odds['oc'] == "*01":
					_0__1_ = _0__1__odds['ov']
			_0__0_ = None
			for _0__0__odds in odds:
				if _0__0__odds['oc'] == "*00":
					_0__0_ = _0__0__odds['ov']
			_2__0_ = None
			for _2__0__odds in odds:
				if _2__0__odds['oc'] == "*20":
					_2__0_ = _2__0__odds['ov']
			_1___2_ = None
			for _1___2__odds in odds:
				if _1___2__odds['oc'] == "*12":
					_1___2_ = _1___2__odds['ov']
			_2__2_ = None
			for _2__2__odds in odds:
				if _2__2__odds['oc'] == "*22":
					_2__2_ = _2__2__odds['ov']
			_0__2_ = None
			for _0__2__odds in odds:
				if _0__2__odds['oc'] == "*02":
					_0__2_ = _0__2__odds['ov']
			_3__1_ = None
			for _3__1__odds in odds:
				if _3__1__odds['oc'] == "*31":
					_3__1_ = _3__1__odds['ov']
			_3__0_ = None
			for _3__0__odds in odds:
				if _3__0__odds['oc'] == "*30":
					_3__0_ = _3__0__odds['ov']
			_1__3_ = None
			for _1__3__odds in odds:
				if _1__3__odds['oc'] == "*13":
					_1__3_ = _1__3__odds['ov']
			_3__2_ = None
			for _3__2__odds in odds:
				if _3__2__odds['oc'] == "*32":
					_3__2_ = _3__2__odds['ov']
			_2__3_ = None
			for _2__3__odds in odds:
				if _2__3__odds['oc'] == "*23":
					_2__3_ = _2__3__odds['ov']
			_0__3_ = None
			for _0__3__odds in odds:
				if _0__3__odds['oc'] == "*03":
					_0__3_ = _0__3__odds['ov']
			_4__1_ = None
			for _4__1__odds in odds:
				if _4__1__odds['oc'] == "*41":
					_4__1_ = _4__1__odds['ov']
			_4__0_ = None
			for _4__0__odds in odds:
				if _4__0__odds['oc'] == "*40":
					_4__0_ = _4__0__odds['ov']
			_3__3_ = None
			for _3__3__odds in odds:
				if _3__3__odds['oc'] == "*33":
					_3__3_ = _3__3__odds['ov']
			_4__2_ = None
			for _4__2__odds in odds:
				if _4__2__odds['oc'] == "*42":
					_4__2_ = _4__2__odds['ov']
			_5__0_ = None
			for _5__0__odds in odds:
				if _5__0__odds['oc'] == "*50":
					_5__0_ = _5__0__odds['ov']
			_5__1_ = None
			for _5__1__odds in odds:
				if _5__1__odds['oc'] == "*51":
					_5__1_ = _5__1__odds['ov']
			_6__0_ = None
			for _6__0__odds in odds:
				if _6__0__odds['oc'] == "*60":
					_6__0_ = _6__0__odds['ov']
			_0__4_ = None
			for _0__4__odds in odds:
				if _0__4__odds['oc'] == "*04":
					_0__4_ = _0__4__odds['ov']
			_1__4_ = None
			for _1__4__odds in odds:
				if _1__4__odds['oc'] == "*14":
					_1__4_ = _1__4__odds['ov']
			_2__4_ = None
			for _2__4__odds in odds:
				if _2__4__odds['oc'] == "*24":
					_2__4_ = _2__4__odds['ov']
			_0__5_ = None
			for _0__5__odds in odds:
				if _0__5__odds['oc'] == "*05":
					_0__5_ = _0__5__odds['ov']
			_1__5_ = None
			for _1__5__odds in odds:
				if _1__5__odds['oc'] == "*15":
					_1__5_ = _1__5__odds['ov']
			_0__6_ = None
			for _0__6__odds in odds:
				if _0__6__odds['oc'] == "*06":
					_0__6_ = _0__6__odds['ov']
			_I1__0_ = None
			for _I1__0__odds in odds:
				if _I1__0__odds['oc'] == "-10":
					_I1__0_ = _I1__0__odds['ov']
			_I2__0_ = None
			for _I2__0__odds in odds:
				if _I2__0__odds['oc'] == "-20":
					_I2__0_ = _I2__0__odds['ov']
			_I2__1_ = None
			for _I2__1__odds in odds:
				if _I2__1__odds['oc'] == "-21":
					_I2__1_ = _I2__1__odds['ov']
			_I1__2_ = None
			for _I1__2__odds in odds:
				if _I1__2__odds['oc'] == "-12":
					_I1__2_ = _I1__2__odds['ov']
			_I0__2_ = None
			for _I0__2__odds in odds:
				if _I0__2__odds['oc'] == "-02":
					_I0__2_ = _I0__2__odds['ov']
			_I0__1_ = None
			for _I0__1__odds in odds:
				if _I0__1__odds['oc'] == "-01":
					_I0__1_ = _I0__1__odds['ov']
			_I0__0_ = None
			for _I0__0__odds in odds:
				if _I0__0__odds['oc'] == "-00":
					_I0__0_ = _I0__0__odds['ov']
			_I1__1_ = None
			for _I1__1__odds in odds:
				if _I1__1__odds['oc'] == "-11":
					_I1__1_ = _I1__1__odds['ov']
			_I2__2_ = None
			for _I2__2__odds in odds:
				if _I2__2__odds['oc'] == "-22":
					_I2__2_ = _I2__2__odds['ov']
			_S2pt00_ = None
			for _S2pt00__odds in odds:
				if _S2pt00__odds['oc'] == "0-2*":
					_S2pt00_ = _S2pt00__odds['ov']
			_P2pt00_ = None
			for _P2pt00__odds in odds:
				if _P2pt00__odds['oc'] == "2+*":
					_P2pt00_ = _P2pt00__odds['ov']
			_S3pt00_ = None
			for _S3pt00__odds in odds:
				if _S3pt00__odds['oc'] == "0-3*":
					_S3pt00_ = _S3pt00__odds['ov']
			_P3pt00_ = None
			for _P3pt00__odds in odds:
				if _P3pt00__odds['oc'] == "3+*":
					_P3pt00_ = _P3pt00__odds['ov']
			_S4pt00_ = None
			for _S4pt00__odds in odds:
				if _S4pt00__odds['oc'] == "0-4*":
					_S4pt00_ = _S4pt00__odds['ov']
			_P4pt00_ = None
			for _P4pt00__odds in odds:
				if _P4pt00__odds['oc'] == "4+*":
					_P4pt00_ = _P4pt00__odds['ov']
			_HA1_1_ = None
			for _HA1_1__odds in odds:
				if _HA1_1__odds['oc'] == "41*":
					_HA1_1_ = _HA1_1__odds['ov']
			_HA2_1_ = None
			for _HA2_1__odds in odds:
				if _HA2_1__odds['oc'] == "42*":
					_HA2_1_ = _HA2_1__odds['ov']
			_PGGsi2p_ = None
			for _PGGsi2p__odds in odds:
				if _PGGsi2p__odds['oc'] == "642":
					_PGGsi2p_ = _PGGsi2p__odds['ov']
			_PGGsi3p_ = None
			for _PGGsi3p__odds in odds:
				if _PGGsi3p__odds['oc'] == "643":
					_PGGsi3p_ = _PGGsi3p__odds['ov']
			_PGGsi4p_ = None
			for _PGGsi4p__odds in odds:
				if _PGGsi4p__odds['oc'] == "644":
					_PGGsi4p_ = _PGGsi4p__odds['ov']
			_PGGsiGG_ = None
			for _PGGsiGG__odds in odds:
				if _PGGsiGG__odds['oc'] == "645":
					_PGGsiGG_ = _PGGsiGG__odds['ov']
			_PGGsiG2p_ = None
			for _PGGsiG2p__odds in odds:
				if _PGGsiG2p__odds['oc'] == "646":
					_PGGsiG2p_ = _PGGsiG2p__odds['ov']
			_PGOsi2p_ = None
			for _PGOsi2p__odds in odds:
				if _PGOsi2p__odds['oc'] == "650":
					_PGOsi2p_ = _PGOsi2p__odds['ov']
			_PGOsi3p_ = None
			for _PGOsi3p__odds in odds:
				if _PGOsi3p__odds['oc'] == "651":
					_PGOsi3p_ = _PGOsi3p__odds['ov']
			_PGOsi4p_ = None
			for _PGOsi4p__odds in odds:
				if _PGOsi4p__odds['oc'] == "652":
					_PGOsi4p_ = _PGOsi4p__odds['ov']
			_PGOsiGG_ = None
			for _PGOsiGG__odds in odds:
				if _PGOsiGG__odds['oc'] == "653":
					_PGOsiGG_ = _PGOsiGG__odds['ov']
			_PGOsiO2p_ = None
			for _PGOsiO2p__odds in odds:
				if _PGOsiO2p__odds['oc'] == "654":
					_PGOsiO2p_ = _PGOsiO2p__odds['ov']
			_Par_ = None
			for _Par__odds in odds:
				if _Par__odds['oc'] == "734":
					_Par_ = _Par__odds['ov']
			_Impar_ = None
			for _Impar__odds in odds:
				if _Impar__odds['oc'] == "735":
					_Impar_ = _Impar__odds['ov']
			_1Xsi0_4_ = None
			for _1Xsi0_4__odds in odds:
				if _1Xsi0_4__odds['oc'] == "351":
					_1Xsi0_4_ = _1Xsi0_4__odds['ov']
			_1XsiII1p_ = None
			for _1XsiII1p__odds in odds:
				if _1XsiII1p__odds['oc'] == "363":
					_1XsiII1p_ = _1XsiII1p__odds['ov']
			_1Xsi0_3_ = None
			for _1Xsi0_3__odds in odds:
				if _1Xsi0_3__odds['oc'] == "135":
					_1Xsi0_3_ = _1Xsi0_3__odds['ov']
			_1Xsi2p_ = None
			for _1Xsi2p__odds in odds:
				if _1Xsi2p__odds['oc'] == "137":
					_1Xsi2p_ = _1Xsi2p__odds['ov']
			_1Xsi2_6_ = None
			for _1Xsi2_6__odds in odds:
				if _1Xsi2_6__odds['oc'] == "355":
					_1Xsi2_6_ = _1Xsi2_6__odds['ov']
			_1Xsi2_5_ = None
			for _1Xsi2_5__odds in odds:
				if _1Xsi2_5__odds['oc'] == "354":
					_1Xsi2_5_ = _1Xsi2_5__odds['ov']
			_1XsiI1p_ = None
			for _1XsiI1p__odds in odds:
				if _1XsiI1p__odds['oc'] == "361":
					_1XsiI1p_ = _1XsiI1p__odds['ov']
			_1Xsi2_4_ = None
			for _1Xsi2_4__odds in odds:
				if _1Xsi2_4__odds['oc'] == "353":
					_1Xsi2_4_ = _1Xsi2_4__odds['ov']
			_1XsiPGG_ = None
			for _1XsiPGG__odds in odds:
				if _1XsiPGG__odds['oc'] == "401":
					_1XsiPGG_ = _1XsiPGG__odds['ov']
			_1Xsi0_2_ = None
			for _1Xsi0_2__odds in odds:
				if _1Xsi0_2__odds['oc'] == "133":
					_1Xsi0_2_ = _1Xsi0_2__odds['ov']
			_1XsiGG_ = None
			for _1XsiGG__odds in odds:
				if _1XsiGG__odds['oc'] == "143":
					_1XsiGG_ = _1XsiGG__odds['ov']
			_1XsiI1psiII1p_ = None
			for _1XsiI1psiII1p__odds in odds:
				if _1XsiI1psiII1p__odds['oc'] == "403":
					_1XsiI1psiII1p_ = _1XsiI1psiII1p__odds['ov']
			_1Xsi3p_ = None
			for _1Xsi3p__odds in odds:
				if _1Xsi3p__odds['oc'] == "139":
					_1Xsi3p_ = _1Xsi3p__odds['ov']
			_1XsiImII_ = None
			for _1XsiImII__odds in odds:
				if _1XsiImII__odds['oc'] == "400":
					_1XsiImII_ = _1XsiImII__odds['ov']
			_1Xsi3_6_ = None
			for _1Xsi3_6__odds in odds:
				if _1Xsi3_6__odds['oc'] == "360":
					_1Xsi3_6_ = _1Xsi3_6__odds['ov']
			_1Xsi3_5_ = None
			for _1Xsi3_5__odds in odds:
				if _1Xsi3_5__odds['oc'] == "356":
					_1Xsi3_5_ = _1Xsi3_5__odds['ov']
			_1Xsi2_3_ = None
			for _1Xsi2_3__odds in odds:
				if _1Xsi2_3__odds['oc'] == "352":
					_1Xsi2_3_ = _1Xsi2_3__odds['ov']
			_1XsiII2p_ = None
			for _1XsiII2p__odds in odds:
				if _1XsiII2p__odds['oc'] == "364":
					_1XsiII2p_ = _1XsiII2p__odds['ov']
			_1XsiIeII_ = None
			for _1XsiIeII__odds in odds:
				if _1XsiIeII__odds['oc'] == "366":
					_1XsiIeII_ = _1XsiIeII__odds['ov']
			_1XsiI2p_ = None
			for _1XsiI2p__odds in odds:
				if _1XsiI2p__odds['oc'] == "362":
					_1XsiI2p_ = _1XsiI2p__odds['ov']
			_1XsiImmII_ = None
			for _1XsiImmII__odds in odds:
				if _1XsiImmII__odds['oc'] == "365":
					_1XsiImmII_ = _1XsiImmII__odds['ov']
			_1XsiPGO_ = None
			for _1XsiPGO__odds in odds:
				if _1XsiPGO__odds['oc'] == "402":
					_1XsiPGO_ = _1XsiPGO__odds['ov']
			_1Xsi4p_ = None
			for _1Xsi4p__odds in odds:
				if _1Xsi4p__odds['oc'] == "346":
					_1Xsi4p_ = _1Xsi4p__odds['ov']
			_1Xsi5p_ = None
			for _1Xsi5p__odds in odds:
				if _1Xsi5p__odds['oc'] == "350":
					_1Xsi5p_ = _1Xsi5p__odds['ov']
			_X2si0_4_ = None
			for _X2si0_4__odds in odds:
				if _X2si0_4__odds['oc'] == "406":
					_X2si0_4_ = _X2si0_4__odds['ov']
			_X2si2p_ = None
			for _X2si2p__odds in odds:
				if _X2si2p__odds['oc'] == "138":
					_X2si2p_ = _X2si2p__odds['ov']
			_X2si2_6_ = None
			for _X2si2_6__odds in odds:
				if _X2si2_6__odds['oc'] == "413":
					_X2si2_6_ = _X2si2_6__odds['ov']
			_X2si2_5_ = None
			for _X2si2_5__odds in odds:
				if _X2si2_5__odds['oc'] == "412":
					_X2si2_5_ = _X2si2_5__odds['ov']
			_X2siI1p_ = None
			for _X2siI1p__odds in odds:
				if _X2siI1p__odds['oc'] == "416":
					_X2siI1p_ = _X2siI1p__odds['ov']
			_X2si2_4_ = None
			for _X2si2_4__odds in odds:
				if _X2si2_4__odds['oc'] == "411":
					_X2si2_4_ = _X2si2_4__odds['ov']
			_X2si0_2_ = None
			for _X2si0_2__odds in odds:
				if _X2si0_2__odds['oc'] == "134":
					_X2si0_2_ = _X2si0_2__odds['ov']
			_X2siGG_ = None
			for _X2siGG__odds in odds:
				if _X2siGG__odds['oc'] == "144":
					_X2siGG_ = _X2siGG__odds['ov']
			_X2siI1psiII1p_ = None
			for _X2siI1psiII1p__odds in odds:
				if _X2siI1psiII1p__odds['oc'] == "431":
					_X2siI1psiII1p_ = _X2siI1psiII1p__odds['ov']
			_X2siPGO_ = None
			for _X2siPGO__odds in odds:
				if _X2siPGO__odds['oc'] == "430":
					_X2siPGO_ = _X2siPGO__odds['ov']
			_X2si3p_ = None
			for _X2si3p__odds in odds:
				if _X2si3p__odds['oc'] == "140":
					_X2si3p_ = _X2si3p__odds['ov']
			_X2si3_6_ = None
			for _X2si3_6__odds in odds:
				if _X2si3_6__odds['oc'] == "415":
					_X2si3_6_ = _X2si3_6__odds['ov']
			_X2siII2p_ = None
			for _X2siII2p__odds in odds:
				if _X2siII2p__odds['oc'] == "422":
					_X2siII2p_ = _X2siII2p__odds['ov']
			_X2si2_3_ = None
			for _X2si2_3__odds in odds:
				if _X2si2_3__odds['oc'] == "410":
					_X2si2_3_ = _X2si2_3__odds['ov']
			_X2siIeII_ = None
			for _X2siIeII__odds in odds:
				if _X2siIeII__odds['oc'] == "424":
					_X2siIeII_ = _X2siIeII__odds['ov']
			_X2siI2p_ = None
			for _X2siI2p__odds in odds:
				if _X2siI2p__odds['oc'] == "420":
					_X2siI2p_ = _X2siI2p__odds['ov']
			_X2siImmII_ = None
			for _X2siImmII__odds in odds:
				if _X2siImmII__odds['oc'] == "423":
					_X2siImmII_ = _X2siImmII__odds['ov']
			_X2siPGG_ = None
			for _X2siPGG__odds in odds:
				if _X2siPGG__odds['oc'] == "426":
					_X2siPGG_ = _X2siPGG__odds['ov']
			_X2si4p_ = None
			for _X2si4p__odds in odds:
				if _X2si4p__odds['oc'] == "404":
					_X2si4p_ = _X2si4p__odds['ov']
			_X2si5p_ = None
			for _X2si5p__odds in odds:
				if _X2si5p__odds['oc'] == "405":
					_X2si5p_ = _X2si5p__odds['ov']
			_X2si0_3_ = None
			for _X2si0_3__odds in odds:
				if _X2si0_3__odds['oc'] == "136":
					_X2si0_3_ = _X2si0_3__odds['ov']
			_X2siII1p_ = None
			for _X2siII1p__odds in odds:
				if _X2siII1p__odds['oc'] == "421":
					_X2siII1p_ = _X2siII1p__odds['ov']
			_X2siImII_ = None
			for _X2siImII__odds in odds:
				if _X2siImII__odds['oc'] == "425":
					_X2siImII_ = _X2siImII__odds['ov']
			_X2si3_5_ = None
			for _X2si3_5__odds in odds:
				if _X2si3_5__odds['oc'] == "414":
					_X2si3_5_ = _X2si3_5__odds['ov']
			_12si0_4_ = None
			for _12si0_4__odds in odds:
				if _12si0_4__odds['oc'] == "441":
					_12si0_4_ = _12si0_4__odds['ov']
			_12siII1p_ = None
			for _12siII1p__odds in odds:
				if _12siII1p__odds['oc'] == "453":
					_12siII1p_ = _12siII1p__odds['ov']
			_12si2_6_ = None
			for _12si2_6__odds in odds:
				if _12si2_6__odds['oc'] == "445":
					_12si2_6_ = _12si2_6__odds['ov']
			_12si2p_ = None
			for _12si2p__odds in odds:
				if _12si2p__odds['oc'] == "432":
					_12si2p_ = _12si2p__odds['ov']
			_12si2_5_ = None
			for _12si2_5__odds in odds:
				if _12si2_5__odds['oc'] == "444":
					_12si2_5_ = _12si2_5__odds['ov']
			_12siI1p_ = None
			for _12siI1p__odds in odds:
				if _12siI1p__odds['oc'] == "451":
					_12siI1p_ = _12siI1p__odds['ov']
			_12si0_3_ = None
			for _12si0_3__odds in odds:
				if _12si0_3__odds['oc'] == "440":
					_12si0_3_ = _12si0_3__odds['ov']
			_12si2_4_ = None
			for _12si2_4__odds in odds:
				if _12si2_4__odds['oc'] == "443":
					_12si2_4_ = _12si2_4__odds['ov']
			_12siI1psiII1p_ = None
			for _12siI1psiII1p__odds in odds:
				if _12siI1psiII1p__odds['oc'] == "464":
					_12siI1psiII1p_ = _12siI1psiII1p__odds['ov']
			_12siPGG_ = None
			for _12siPGG__odds in odds:
				if _12siPGG__odds['oc'] == "462":
					_12siPGG_ = _12siPGG__odds['ov']
			_12si3p_ = None
			for _12si3p__odds in odds:
				if _12si3p__odds['oc'] == "433":
					_12si3p_ = _12si3p__odds['ov']
			_12siII2p_ = None
			for _12siII2p__odds in odds:
				if _12siII2p__odds['oc'] == "454":
					_12siII2p_ = _12siII2p__odds['ov']
			_12si0_2_ = None
			for _12si0_2__odds in odds:
				if _12si0_2__odds['oc'] == "436":
					_12si0_2_ = _12si0_2__odds['ov']
			_12si3_6_ = None
			for _12si3_6__odds in odds:
				if _12si3_6__odds['oc'] == "450":
					_12si3_6_ = _12si3_6__odds['ov']
			_12siImII_ = None
			for _12siImII__odds in odds:
				if _12siImII__odds['oc'] == "461":
					_12siImII_ = _12siImII__odds['ov']
			_12siGG_ = None
			for _12siGG__odds in odds:
				if _12siGG__odds['oc'] == "455":
					_12siGG_ = _12siGG__odds['ov']
			_12siPGO_ = None
			for _12siPGO__odds in odds:
				if _12siPGO__odds['oc'] == "463":
					_12siPGO_ = _12siPGO__odds['ov']
			_12siI2p_ = None
			for _12siI2p__odds in odds:
				if _12siI2p__odds['oc'] == "452":
					_12siI2p_ = _12siI2p__odds['ov']
			_12siImmII_ = None
			for _12siImmII__odds in odds:
				if _12siImmII__odds['oc'] == "456":
					_12siImmII_ = _12siImmII__odds['ov']
			_12si4p_ = None
			for _12si4p__odds in odds:
				if _12si4p__odds['oc'] == "434":
					_12si4p_ = _12si4p__odds['ov']
			_12siIeII_ = None
			for _12siIeII__odds in odds:
				if _12siIeII__odds['oc'] == "460":
					_12siIeII_ = _12siIeII__odds['ov']
			_12si5p_ = None
			for _12si5p__odds in odds:
				if _12si5p__odds['oc'] == "435":
					_12si5p_ = _12si5p__odds['ov']
			_12si2_3_ = None
			for _12si2_3__odds in odds:
				if _12si2_3__odds['oc'] == "442":
					_12si2_3_ = _12si2_3__odds['ov']
			_12si3_5_ = None
			for _12si3_5__odds in odds:
				if _12si3_5__odds['oc'] == "446":
					_12si3_5_ = _12si3_5__odds['ov']
			_1_1si0_4_ = None
			for _1_1si0_4__odds in odds:
				if _1_1si0_4__odds['oc'] == "502":
					_1_1si0_4_ = _1_1si0_4__odds['ov']
			_1_1si2p_ = None
			for _1_1si2p__odds in odds:
				if _1_1si2p__odds['oc'] == "465":
					_1_1si2p_ = _1_1si2p__odds['ov']
			_1_1si2_6_ = None
			for _1_1si2_6__odds in odds:
				if _1_1si2_6__odds['oc'] == "506":
					_1_1si2_6_ = _1_1si2_6__odds['ov']
			_1_1si2_5_ = None
			for _1_1si2_5__odds in odds:
				if _1_1si2_5__odds['oc'] == "505":
					_1_1si2_5_ = _1_1si2_5__odds['ov']
			_1_1si0_3_ = None
			for _1_1si0_3__odds in odds:
				if _1_1si0_3__odds['oc'] == "501":
					_1_1si0_3_ = _1_1si0_3__odds['ov']
			_X_Xsi0_2_ = None
			for _X_Xsi0_2__odds in odds:
				if _X_Xsi0_2__odds['oc'] == "631":
					_X_Xsi0_2_ = _X_Xsi0_2__odds['ov']
			_1_1si2_4_ = None
			for _1_1si2_4__odds in odds:
				if _1_1si2_4__odds['oc'] == "504":
					_1_1si2_4_ = _1_1si2_4__odds['ov']
			_X_1si0_4_ = None
			for _X_1si0_4__odds in odds:
				if _X_1si0_4__odds['oc'] == "542":
					_X_1si0_4_ = _X_1si0_4__odds['ov']
			_2_2si0_4_ = None
			for _2_2si0_4__odds in odds:
				if _2_2si0_4__odds['oc'] == "521":
					_2_2si0_4_ = _2_2si0_4__odds['ov']
			_X_Xsi2p_ = None
			for _X_Xsi2p__odds in odds:
				if _X_Xsi2p__odds['oc'] == "626":
					_X_Xsi2p_ = _X_Xsi2p__odds['ov']
			_1_1si3p_ = None
			for _1_1si3p__odds in odds:
				if _1_1si3p__odds['oc'] == "96":
					_1_1si3p_ = _1_1si3p__odds['ov']
			_1_1siNGG_ = None
			for _1_1siNGG__odds in odds:
				if _1_1siNGG__odds['oc'] == "513":
					_1_1siNGG_ = _1_1siNGG__odds['ov']
			_1_1si3_6_ = None
			for _1_1si3_6__odds in odds:
				if _1_1si3_6__odds['oc'] == "511":
					_1_1si3_6_ = _1_1si3_6__odds['ov']
			_2_2si2p_ = None
			for _2_2si2p__odds in odds:
				if _2_2si2p__odds['oc'] == "514":
					_2_2si2p_ = _2_2si2p__odds['ov']
			_2_2si2_6_ = None
			for _2_2si2_6__odds in odds:
				if _2_2si2_6__odds['oc'] == "525":
					_2_2si2_6_ = _2_2si2_6__odds['ov']
			_X_Xsi2_4_ = None
			for _X_Xsi2_4__odds in odds:
				if _X_Xsi2_4__odds['oc'] == "632":
					_X_Xsi2_4_ = _X_Xsi2_4__odds['ov']
			_X_1si2p_ = None
			for _X_1si2p__odds in odds:
				if _X_1si2p__odds['oc'] == "533":
					_X_1si2p_ = _X_1si2p__odds['ov']
			_1_1si2_3_ = None
			for _1_1si2_3__odds in odds:
				if _1_1si2_3__odds['oc'] == "503":
					_1_1si2_3_ = _1_1si2_3__odds['ov']
			_X_1si2_6_ = None
			for _X_1si2_6__odds in odds:
				if _X_1si2_6__odds['oc'] == "546":
					_X_1si2_6_ = _X_1si2_6__odds['ov']
			_1_1siII2p_ = None
			for _1_1siII2p__odds in odds:
				if _1_1siII2p__odds['oc'] == "512":
					_1_1siII2p_ = _1_1siII2p__odds['ov']
			_2_2si2_5_ = None
			for _2_2si2_5__odds in odds:
				if _2_2si2_5__odds['oc'] == "524":
					_2_2si2_5_ = _2_2si2_5__odds['ov']
			_2_2si0_3_ = None
			for _2_2si0_3__odds in odds:
				if _2_2si0_3__odds['oc'] == "520":
					_2_2si0_3_ = _2_2si0_3__odds['ov']
			_X_1si2_5_ = None
			for _X_1si2_5__odds in odds:
				if _X_1si2_5__odds['oc'] == "545":
					_X_1si2_5_ = _X_1si2_5__odds['ov']
			_X_2si0_4_ = None
			for _X_2si0_4__odds in odds:
				if _X_2si0_4__odds['oc'] == "566":
					_X_2si0_4_ = _X_2si0_4__odds['ov']
			_2_2si2_4_ = None
			for _2_2si2_4__odds in odds:
				if _2_2si2_4__odds['oc'] == "523":
					_2_2si2_4_ = _2_2si2_4__odds['ov']
			_X_1si2_4_ = None
			for _X_1si2_4__odds in odds:
				if _X_1si2_4__odds['oc'] == "544":
					_X_1si2_4_ = _X_1si2_4__odds['ov']
			_1_1siGG_ = None
			for _1_1siGG__odds in odds:
				if _1_1siGG__odds['oc'] == "147":
					_1_1siGG_ = _1_1siGG__odds['ov']
			_X_1siNGG_ = None
			for _X_1siNGG__odds in odds:
				if _X_1siNGG__odds['oc'] == "555":
					_X_1siNGG_ = _X_1siNGG__odds['ov']
			_X_2si0_3_ = None
			for _X_2si0_3__odds in odds:
				if _X_2si0_3__odds['oc'] == "565":
					_X_2si0_3_ = _X_2si0_3__odds['ov']
			_1_1si0_2_ = None
			for _1_1si0_2__odds in odds:
				if _1_1si0_2__odds['oc'] == "500":
					_1_1si0_2_ = _1_1si0_2__odds['ov']
			_2_2siNGG_ = None
			for _2_2siNGG__odds in odds:
				if _2_2siNGG__odds['oc'] == "531":
					_2_2siNGG_ = _2_2siNGG__odds['ov']
			_X_2si2p_ = None
			for _X_2si2p__odds in odds:
				if _X_2si2p__odds['oc'] == "560":
					_X_2si2p_ = _X_2si2p__odds['ov']
			_X_2si2_6_ = None
			for _X_2si2_6__odds in odds:
				if _X_2si2_6__odds['oc'] == "606":
					_X_2si2_6_ = _X_2si2_6__odds['ov']
			_2_2si3_6_ = None
			for _2_2si3_6__odds in odds:
				if _2_2si3_6__odds['oc'] == "526":
					_2_2si3_6_ = _2_2si3_6__odds['ov']
			_X_2si2_5_ = None
			for _X_2si2_5__odds in odds:
				if _X_2si2_5__odds['oc'] == "605":
					_X_2si2_5_ = _X_2si2_5__odds['ov']
			_2_2si3_5_ = None
			for _2_2si3_5__odds in odds:
				if _2_2si3_5__odds['oc'] == "527":
					_2_2si3_5_ = _2_2si3_5__odds['ov']
			_1_1siI2p_ = None
			for _1_1siI2p__odds in odds:
				if _1_1siI2p__odds['oc'] == "901":
					_1_1siI2p_ = _1_1siI2p__odds['ov']
			_X_2siNGG_ = None
			for _X_2siNGG__odds in odds:
				if _X_2siNGG__odds['oc'] == "624":
					_X_2siNGG_ = _X_2siNGG__odds['ov']
			_2_2siII2p_ = None
			for _2_2siII2p__odds in odds:
				if _2_2siII2p__odds['oc'] == "530":
					_2_2siII2p_ = _2_2siII2p__odds['ov']
			_X_2si5p_ = None
			for _X_2si5p__odds in odds:
				if _X_2si5p__odds['oc'] == "563":
					_X_2si5p_ = _X_2si5p__odds['ov']
			_2_2si2_3_ = None
			for _2_2si2_3__odds in odds:
				if _2_2si2_3__odds['oc'] == "522":
					_2_2si2_3_ = _2_2si2_3__odds['ov']
			_X_1siGG_ = None
			for _X_1siGG__odds in odds:
				if _X_1siGG__odds['oc'] == "554":
					_X_1siGG_ = _X_1siGG__odds['ov']
			_X_1si2_3_ = None
			for _X_1si2_3__odds in odds:
				if _X_1si2_3__odds['oc'] == "543":
					_X_1si2_3_ = _X_1si2_3__odds['ov']
			_X_2si0_2_ = None
			for _X_2si0_2__odds in odds:
				if _X_2si0_2__odds['oc'] == "564":
					_X_2si0_2_ = _X_2si0_2__odds['ov']
			_X_1si3_6_ = None
			for _X_1si3_6__odds in odds:
				if _X_1si3_6__odds['oc'] == "551":
					_X_1si3_6_ = _X_1si3_6__odds['ov']
			_1_1si4p_ = None
			for _1_1si4p__odds in odds:
				if _1_1si4p__odds['oc'] == "145":
					_1_1si4p_ = _1_1si4p__odds['ov']
			_2_2si0_2_ = None
			for _2_2si0_2__odds in odds:
				if _2_2si0_2__odds['oc'] == "516":
					_2_2si0_2_ = _2_2si0_2__odds['ov']
			_X_1si3_5_ = None
			for _X_1si3_5__odds in odds:
				if _X_1si3_5__odds['oc'] == "550":
					_X_1si3_5_ = _X_1si3_5__odds['ov']
			_X_2siII2p_ = None
			for _X_2siII2p__odds in odds:
				if _X_2siII2p__odds['oc'] == "616":
					_X_2siII2p_ = _X_2siII2p__odds['ov']
			_X_2siGG_ = None
			for _X_2siGG__odds in odds:
				if _X_2siGG__odds['oc'] == "623":
					_X_2siGG_ = _X_2siGG__odds['ov']
			_X_1siI2p_ = None
			for _X_1siI2p__odds in odds:
				if _X_1siI2p__odds['oc'] == "552":
					_X_1siI2p_ = _X_1siI2p__odds['ov']
			_X_XsiI2p_ = None
			for _X_XsiI2p__odds in odds:
				if _X_XsiI2p__odds['oc'] == "633":
					_X_XsiI2p_ = _X_XsiI2p__odds['ov']
			_X_2si3p_ = None
			for _X_2si3p__odds in odds:
				if _X_2si3p__odds['oc'] == "561":
					_X_2si3p_ = _X_2si3p__odds['ov']
			_X_2si3_6_ = None
			for _X_2si3_6__odds in odds:
				if _X_2si3_6__odds['oc'] == "614":
					_X_2si3_6_ = _X_2si3_6__odds['ov']
			_X_2si3_5_ = None
			for _X_2si3_5__odds in odds:
				if _X_2si3_5__odds['oc'] == "613":
					_X_2si3_5_ = _X_2si3_5__odds['ov']
			_2_2si4p_ = None
			for _2_2si4p__odds in odds:
				if _2_2si4p__odds['oc'] == "146":
					_2_2si4p_ = _2_2si4p__odds['ov']
			_X_2siI2p_ = None
			for _X_2siI2p__odds in odds:
				if _X_2siI2p__odds['oc'] == "615":
					_X_2siI2p_ = _X_2siI2p__odds['ov']
			_X_1si4p_ = None
			for _X_1si4p__odds in odds:
				if _X_1si4p__odds['oc'] == "535":
					_X_1si4p_ = _X_1si4p__odds['ov']
			_1_1si5p_ = None
			for _1_1si5p__odds in odds:
				if _1_1si5p__odds['oc'] == "466":
					_1_1si5p_ = _1_1si5p__odds['ov']
			_X_2si4p_ = None
			for _X_2si4p__odds in odds:
				if _X_2si4p__odds['oc'] == "562":
					_X_2si4p_ = _X_2si4p__odds['ov']
			_X_Xsi4p_ = None
			for _X_Xsi4p__odds in odds:
				if _X_Xsi4p__odds['oc'] == "630":
					_X_Xsi4p_ = _X_Xsi4p__odds['ov']
			_2_2si5p_ = None
			for _2_2si5p__odds in odds:
				if _2_2si5p__odds['oc'] == "515":
					_2_2si5p_ = _2_2si5p__odds['ov']
			_X_1si5p_ = None
			for _X_1si5p__odds in odds:
				if _X_1si5p__odds['oc'] == "536":
					_X_1si5p_ = _X_1si5p__odds['ov']
			_2_1si4p_ = None
			for _2_1si4p__odds in odds:
				if _2_1si4p__odds['oc'] == "640":
					_2_1si4p_ = _2_1si4p__odds['ov']
			_1_2si4p_ = None
			for _1_2si4p__odds in odds:
				if _1_2si4p__odds['oc'] == "635":
					_1_2si4p_ = _1_2si4p__odds['ov']
			_2_1si5p_ = None
			for _2_1si5p__odds in odds:
				if _2_1si5p__odds['oc'] == "641":
					_2_1si5p_ = _2_1si5p__odds['ov']
			_1_2si5p_ = None
			for _1_2si5p__odds in odds:
				if _1_2si5p__odds['oc'] == "636":
					_1_2si5p_ = _1_2si5p__odds['ov']
			_1_1si3_5_ = None
			for _1_1si3_5__odds in odds:
				if _1_1si3_5__odds['oc'] == "510":
					_1_1si3_5_ = _1_1si3_5__odds['ov']
			_X_1si0_3_ = None
			for _X_1si0_3__odds in odds:
				if _X_1si0_3__odds['oc'] == "541":
					_X_1si0_3_ = _X_1si0_3__odds['ov']
			_2_2si3p_ = None
			for _2_2si3p__odds in odds:
				if _2_2si3p__odds['oc'] == "97":
					_2_2si3p_ = _2_2si3p__odds['ov']
			_X_1si0_2_ = None
			for _X_1si0_2__odds in odds:
				if _X_1si0_2__odds['oc'] == "540":
					_X_1si0_2_ = _X_1si0_2__odds['ov']
			_X_1siII2p_ = None
			for _X_1siII2p__odds in odds:
				if _X_1siII2p__odds['oc'] == "553":
					_X_1siII2p_ = _X_1siII2p__odds['ov']
			_X_2si2_4_ = None
			for _X_2si2_4__odds in odds:
				if _X_2si2_4__odds['oc'] == "604":
					_X_2si2_4_ = _X_2si2_4__odds['ov']
			_X_XsiII2p_ = None
			for _X_XsiII2p__odds in odds:
				if _X_XsiII2p__odds['oc'] == "634":
					_X_XsiII2p_ = _X_XsiII2p__odds['ov']
			_2_2siGG_ = None
			for _2_2siGG__odds in odds:
				if _2_2siGG__odds['oc'] == "148":
					_2_2siGG_ = _2_2siGG__odds['ov']
			_X_1si3p_ = None
			for _X_1si3p__odds in odds:
				if _X_1si3p__odds['oc'] == "534":
					_X_1si3p_ = _X_1si3p__odds['ov']
			_2_2siI2p_ = None
			for _2_2siI2p__odds in odds:
				if _2_2siI2p__odds['oc'] == "902":
					_2_2siI2p_ = _2_2siI2p__odds['ov']
			_X_2si2_3_ = None
			for _X_2si2_3__odds in odds:
				if _X_2si2_3__odds['oc'] == "603":
					_X_2si2_3_ = _X_2si2_3__odds['ov']
			_1siPGG_ = None
			for _1siPGG__odds in odds:
				if _1siPGG__odds['oc'] == "303":
					_1siPGG_ = _1siPGG__odds['ov']
			_2siPGO_ = None
			for _2siPGO__odds in odds:
				if _2siPGO__odds['oc'] == "344":
					_2siPGO_ = _2siPGO__odds['ov']
			_1siPGO_ = None
			for _1siPGO__odds in odds:
				if _1siPGO__odds['oc'] == "304":
					_1siPGO_ = _1siPGO__odds['ov']
			_2siPGG_ = None
			for _2siPGG__odds in odds:
				if _2siPGG__odds['oc'] == "343":
					_2siPGG_ = _2siPGG__odds['ov']
			_VSG_ = None
			for _VSG__odds in odds:
				if _VSG__odds['oc'] == "731":
					_VSG_ = _VSG__odds['ov']
			_VSO_ = None
			for _VSO__odds in odds:
				if _VSO__odds['oc'] == "732":
					_VSO_ = _VSO__odds['ov']
			_VDG_ = None
			for _VDG__odds in odds:
				if _VDG__odds['oc'] == "911":
					_VDG_ = _VDG__odds['ov']
			_VSDG_ = None
			for _VSDG__odds in odds:
				if _VSDG__odds['oc'] == "913":
					_VSDG_ = _VSDG__odds['ov']
			_VDO_ = None
			for _VDO__odds in odds:
				if _VDO__odds['oc'] == "912":
					_VDO_ = _VDO__odds['ov']
			_VDGsi4p_ = None
			for _VDGsi4p__odds in odds:
				if _VDGsi4p__odds['oc'] == "915":
					_VDGsi4p_ = _VDGsi4p__odds['ov']
			_VSDO_ = None
			for _VSDO__odds in odds:
				if _VSDO__odds['oc'] == "914":
					_VSDO_ = _VSDO__odds['ov']
			_VDOsi4p_ = None
			for _VDOsi4p__odds in odds:
				if _VDOsi4p__odds['oc'] == "916":
					_VDOsi4p_ = _VDOsi4p__odds['ov']
			_Xsau3p_ = None
			for _Xsau3p__odds in odds:
				if _Xsau3p__odds['oc'] == "18":
					_Xsau3p_ = _Xsau3p__odds['ov']
			_1sau3p_ = None
			for _1sau3p__odds in odds:
				if _1sau3p__odds['oc'] == "13":
					_1sau3p_ = _1sau3p__odds['ov']
			_GGsau3p_ = None
			for _GGsau3p__odds in odds:
				if _GGsau3p__odds['oc'] == "33":
					_GGsau3p_ = _GGsau3p__odds['ov']
			_IXsauIIX_ = None
			for _IXsauIIX__odds in odds:
				if _IXsauIIX__odds['oc'] == "3":
					_IXsauIIX_ = _IXsauIIX__odds['ov']
			_NGGsau0_2_ = None
			for _NGGsau0_2__odds in odds:
				if _NGGsau0_2__odds['oc'] == "27":
					_NGGsau0_2_ = _NGGsau0_2__odds['ov']
			_2sau3p_ = None
			for _2sau3p__odds in odds:
				if _2sau3p__odds['oc'] == "23":
					_2sau3p_ = _2sau3p__odds['ov']
			_I2psauII2p_ = None
			for _I2psauII2p__odds in odds:
				if _I2psauII2p__odds['oc'] == "19":
					_I2psauII2p_ = _I2psauII2p__odds['ov']
			_I1sauII1_ = None
			for _I1sauII1__odds in odds:
				if _I1sauII1__odds['oc'] == "1":
					_I1sauII1_ = _I1sauII1__odds['ov']
			_2sau4p_ = None
			for _2sau4p__odds in odds:
				if _2sau4p__odds['oc'] == "24":
					_2sau4p_ = _2sau4p__odds['ov']
			_I2sauII2_ = None
			for _I2sauII2__odds in odds:
				if _I2sauII2__odds['oc'] == "2":
					_I2sauII2_ = _I2sauII2__odds['ov']
			_IGGsauIIGG_ = None
			for _IGGsauIIGG__odds in odds:
				if _IGGsauIIGG__odds['oc'] == "36":
					_IGGsauIIGG_ = _IGGsauIIGG__odds['ov']
			_I2psau4p_ = None
			for _I2psau4p__odds in odds:
				if _I2psau4p__odds['oc'] == "25":
					_I2psau4p_ = _I2psau4p__odds['ov']
			_1_1sau2_2_ = None
			for _1_1sau2_2__odds in odds:
				if _1_1sau2_2__odds['oc'] == "29":
					_1_1sau2_2_ = _1_1sau2_2__odds['ov']
			_1_1sauX_1_ = None
			for _1_1sauX_1__odds in odds:
				if _1_1sauX_1__odds['oc'] == "28":
					_1_1sauX_1_ = _1_1sauX_1__odds['ov']
			_X_XsauX_1_ = None
			for _X_XsauX_1__odds in odds:
				if _X_XsauX_1__odds['oc'] == "35":
					_X_XsauX_1_ = _X_XsauX_1__odds['ov']
			_X_XsauX_2_ = None
			for _X_XsauX_2__odds in odds:
				if _X_XsauX_2__odds['oc'] == "37":
					_X_XsauX_2_ = _X_XsauX_2__odds['ov']
			_X_1sauX_2_ = None
			for _X_1sauX_2__odds in odds:
				if _X_1sauX_2__odds['oc'] == "38":
					_X_1sauX_2_ = _X_1sauX_2__odds['ov']
			_2_2sauX_2_ = None
			for _2_2sauX_2__odds in odds:
				if _2_2sauX_2__odds['oc'] == "34":
					_2_2sauX_2_ = _2_2sauX_2__odds['ov']
			_I3psauII3p_ = None
			for _I3psauII3p__odds in odds:
				if _I3psauII3p__odds['oc'] == "26":
					_I3psauII3p_ = _I3psauII3p__odds['ov']
			_1sau4p_ = None
			for _1sau4p__odds in odds:
				if _1sau4p__odds['oc'] == "14":
					_1sau4p_ = _1sau4p__odds['ov']
			_2sauI2p_ = None
			for _2sauI2p__odds in odds:
				if _2sauI2p__odds['oc'] == "16":
					_2sauI2p_ = _2sauI2p__odds['ov']
			_1sauI2p_ = None
			for _1sauI2p__odds in odds:
				if _1sauI2p__odds['oc'] == "15":
					_1sauI2p_ = _1sauI2p__odds['ov']
			_Xsau0_2_ = None
			for _Xsau0_2__odds in odds:
				if _Xsau0_2__odds['oc'] == "17":
					_Xsau0_2_ = _Xsau0_2__odds['ov']
			# _SC_1_ = None
			# for _SC_1__odds in odds:
			# 	if _SC_1__odds['oc'] == "+11":
			# 		_SC_1_ = _SC_1__odds['ov']
			# _SC_X_ = None
			# for _SC_X__odds in odds:
			# 	if _SC_X__odds['oc'] == "+10":
			# 		_SC_X_ = _SC_X__odds['ov']
			# _SC_2_ = None
			# for _SC_2__odds in odds:
			# 	if _SC_2__odds['oc'] == "+12":
			# 		_SC_2_ = _SC_2__odds['ov']
			# _SC_1X_ = None
			# for _SC_1X__odds in odds:
			# 	if _SC_1X__odds['oc'] == "+110":
			# 		_SC_1X_ = _SC_1X__odds['ov']
			# _SC_X2_ = None
			# for _SC_X2__odds in odds:
			# 	if _SC_X2__odds['oc'] == "+102":
			# 		_SC_X2_ = _SC_X2__odds['ov']
			# _SC_12_ = None
			# for _SC_12__odds in odds:
			# 	if _SC_12__odds['oc'] == "+112":
			# 		_SC_12_ = _SC_12__odds['ov']
			# _SE_1_ = None
			# for _SE_1__odds in odds:
			# 	if _SE_1__odds['oc'] == "+11":
			# 		_SE_1_ = _SE_1__odds['ov']
			# _SE_X_ = None
			# for _SE_X__odds in odds:
			# 	if _SE_X__odds['oc'] == "+10":
			# 		_SE_X_ = _SE_X__odds['ov']
			# _SE_2_ = None
			# for _SE_2__odds in odds:
			# 	if _SE_2__odds['oc'] == "+12":
			# 		_SE_2_ = _SE_2__odds['ov']
			# _SE_1X_ = None
			# for _SE_1X__odds in odds:
			# 	if _SE_1X__odds['oc'] == "+110":
			# 		_SE_1X_ = _SE_1X__odds['ov']
			# _SE_X2_ = None
			# for _SE_X2__odds in odds:
			# 	if _SE_X2__odds['oc'] == "+102":
			# 		_SE_X2_ = _SE_X2__odds['ov']
			# _SE_12_ = None
			# for _SE_12__odds in odds:
			# 	if _SE_12__odds['oc'] == "+112":
			# 		_SE_12_ = _SE_12__odds['ov']




			yield {              
				'country': country,
				'league': league,
				'home': home,
				'away': away,				
				'dt': dt,
				'_1_': _1_,
				'_X_': _X_,
				'_2_': _2_,
				'_1X_': _1X_,
				'_X2_': _X2_,
				'_12_': _12_,
				's_id': s_id,  
				'_1_1_': _1_1_,
				'_1_X_': _1_X_,
				'_1_2_': _1_2_,
				'_X_1_': _X_1_,
				'_X_X_': _X_X_,
				'_X_2_': _X_2_,
				'_2_1_': _2_1_,
				'_2_X_': _2_X_,
				'_2_2_': _2_2_,
				'_1_1X_': _1_1X_,
				'_1_X2_': _1_X2_,
				'_1_12_': _1_12_,
				'_X_1X_': _X_1X_,
				'_X_X2_': _X_X2_,
				'_X_12_': _X_12_,
				'_2_1X_': _2_1X_,
				'_2_X2_': _2_X2_,
				'_2_12_': _2_12_,
				'_1X_1_': _1X_1_,
				'_1X_X_': _1X_X_,
				'_1X_2_': _1X_2_,
				'_X2_1_': _X2_1_,
				'_X2_X_': _X2_X_,
				'_X2_2_': _X2_2_,
				'_12_1_': _12_1_,
				'_12_X_': _12_X_,
				'_12_2_': _12_2_,
				'_NUX_2_': _NUX_2_,
				'_NUX_X_': _NUX_X_,
				'_NU1_1_': _NU1_1_,
				'_1X_1X_': _1X_1X_,
				'_1X_12_': _1X_12_,
				'_X2_X2_': _X2_X2_,
				'_X2_12_': _X2_12_,
				'_12_12_': _12_12_,
				'_X2_1X_': _X2_1X_,
				'_1X_X2_': _1X_X2_,
				'_12_1X_': _12_1X_,
				'_12_X2_': _12_X2_,
				'_NU2_2_': _NU2_2_,
				'_NUX_1_': _NUX_1_,
				'_I1_': _I1_,
				'_IX_': _IX_,
				'_I2_': _I2_,
				'_I1X_': _I1X_,
				'_IX2_': _IX2_,
				'_I12_': _I12_,
				'_II1_': _II1_,
				'_IIX_': _IIX_,
				'_II2_': _II2_,
				'_II1X_': _II1X_,
				'_IIX2_': _IIX2_,
				'_II12_': _II12_,
				'_PsF1_': _PsF1_,
				'_PsFX_': _PsFX_,
				'_PsF2_': _PsF2_,
				'_H1_1pt5_': _H1_1pt5_,
				'_H2_1pt5_': _H2_1pt5_,
				'_DNB1_': _DNB1_,
				'_IDNB1_': _IDNB1_,
				'_DNB2_': _DNB2_,
				'_IDNB2_': _IDNB2_,
				'_0_1_': _0_1_,
				'_0_2_': _0_2_,
				'_0_3_': _0_3_,
				'_0_4_': _0_4_,
				'_0_5_': _0_5_,
				'_1__2_': _1__2_,
				'_1_3_': _1_3_,
				'_1_4_': _1_4_,
				'_1_5_': _1_5_,
				'_1_6_': _1_6_,
				'_2_3_': _2_3_,
				'_2_4_': _2_4_,
				'_2_5_': _2_5_,
				'_2_6_': _2_6_,
				'_3_4_': _3_4_,
				'_3_5_': _3_5_,
				'_3_6_': _3_6_,
				'_4_5_': _4_5_,
				'_4_6_': _4_6_,
				'_1p_': _1p_,
				'_2p_': _2p_,
				'_3p_': _3p_,
				'_4p_': _4p_,
				'_5p_': _5p_,
				'_6p_': _6p_,
				'_7p_': _7p_,
				'_E2_': _E2_,
				'_E3_': _E3_,
				'_E4_': _E4_,
				'_NE2_': _NE2_,
				'_NE3_': _NE3_,
				'_NE4_': _NE4_,
				'_NE1_': _NE1_,
				'_I0_1_': _I0_1_,
				'_I0_2_': _I0_2_,
				'_I1_2_': _I1_2_,
				'_I1_3_': _I1_3_,
				'_I2_3_': _I2_3_,
				'_I1p_': _I1p_,
				'_I2p_': _I2p_,
				'_I3p_': _I3p_,
				'_I4p_': _I4p_,
				'_IE1_': _IE1_,
				'_IE2_': _IE2_,
				'_INE1_': _INE1_,
				'_INE2_': _INE2_,
				'_II0_1_': _II0_1_,
				'_II0_3_': _II0_3_,
				'_II0_2_': _II0_2_,
				'_II1_2_': _II1_2_,
				'_II1_3_': _II1_3_,
				'_II2_3_': _II2_3_,
				'_II1p_': _II1p_,
				'_II2p_': _II2p_,
				'_II3p_': _II3p_,
				'_II4p_': _II4p_,
				'_IIE1_': _IIE1_,
				'_IIE2_': _IIE2_,
				'_IINE1_': _IINE1_,
				'_IINE2_': _IINE2_,
				'_INGG_': _INGG_,
				'_NGG4p_': _NGG4p_,
				'_IINGG_': _IINGG_,
				'_INGGsiIINGG_': _INGGsiIINGG_,
				'_NGG3p_': _NGG3p_,
				'_GG_': _GG_,
				'_GGsi2_4_': _GGsi2_4_,
				'_NGG_': _NGG_,
				'_GG3p_': _GG3p_,
				'_GGsi3_6_': _GGsi3_6_,
				'_GGsi3_5_': _GGsi3_5_,
				'_GGsi2_3_': _GGsi2_3_,
				'_GGsiG2p_': _GGsiG2p_,
				'_IIGG_': _IIGG_,
				'_GGsiO2p_': _GGsiO2p_,
				'_GG4p_': _GG4p_,
				'_INGGsiIIGG_': _INGGsiIIGG_,
				'_IGG_': _IGG_,
				'_IGGsiIINGG_': _IGGsiIINGG_,
				'_G2pO2p_': _G2pO2p_,
				'_IGGsiIIGG_': _IGGsiIIGG_,
				'_I0_3siII0_3_': _I0_3siII0_3_,
				'_I0_2siII0_3_': _I0_2siII0_3_,
				'_I0_3siII0_2_': _I0_3siII0_2_,
				'_I0_2siII0_2_': _I0_2siII0_2_,
				'_I0_1siII0_3_': _I0_1siII0_3_,
				'_I1psi2p_': _I1psi2p_,
				'_I0_1siII0_2_': _I0_1siII0_2_,
				'_I0_3siII0_1_': _I0_3siII0_1_,
				'_I0_2siII0_1_': _I0_2siII0_1_,
				'_I1psiII1p_': _I1psiII1p_,
				'_I0_1siII0_1_': _I0_1siII0_1_,
				'_I1psi3p_': _I1psi3p_,
				'_I1psiII2p_': _I1psiII2p_,
				'_I2psi3p_': _I2psi3p_,
				'_I2psiII1p_': _I2psiII1p_,
				'_I1psi4p_': _I1psi4p_,
				'_I2psi4p_': _I2psi4p_,
				'_I2psiII2p_': _I2psiII2p_,
				'_I1psiII3p_': _I1psiII3p_,
				'_I3psiII1p_': _I3psiII1p_,
				'_I2psi5p_': _I2psi5p_,
				'_I2psiII3p_': _I2psiII3p_,
				'_I3psiII2p_': _I3psiII2p_,
				'_I3psiII3p_': _I3psiII3p_,
				'_PGG_': _PGG_,
				'_PGO_': _PGO_,
				'_G0_2_': _G0_2_,
				'_GNE2_': _GNE2_,
				'_G1p_': _G1p_,
				'_G1_3_': _G1_3_,
				'_GNE1_': _GNE1_,
				'_G0_1_': _G0_1_,
				'_G1_2_': _G1_2_,
				'_G2p_': _G2p_,
				'_GE1_': _GE1_,
				'_G2_3_': _G2_3_,
				'_GNG_': _GNG_,
				'_GE2_': _GE2_,
				'_G3p_': _G3p_,
				'_G4p_': _G4p_,
				'_O0_2_': _O0_2_,
				'_ONE2_': _ONE2_,
				'_O0_1_': _O0_1_,
				'_O1p_': _O1p_,
				'_O1_3_': _O1_3_,
				'_ONE1_': _ONE1_,
				'_O1_2_': _O1_2_,
				'_OE1_': _OE1_,
				'_ONG_': _ONG_,
				'_O2p_': _O2p_,
				'_O2_3_': _O2_3_,
				'_OE2_': _OE2_,
				'_O3p_': _O3p_,
				'_O4p_': _O4p_,
				'_O0_3_': _O0_3_,
				'_IG0_1_': _IG0_1_,
				'_IGNG_': _IGNG_,
				'_IG1p_': _IG1p_,
				'_IG1_2_': _IG1_2_,
				'_IG2p_': _IG2p_,
				'_IG3p_': _IG3p_,
				'_IO0_1_': _IO0_1_,
				'_IONG_': _IONG_,
				'_IO1p_': _IO1p_,
				'_IO1_2_': _IO1_2_,
				'_IO2p_': _IO2p_,
				'_IO3p_': _IO3p_,
				'_IIG0_1_': _IIG0_1_,
				'_IIG1p_': _IIG1p_,
				'_IIG1_2_': _IIG1_2_,
				'_IIGNG_': _IIGNG_,
				'_IIG2p_': _IIG2p_,
				'_IIG3p_': _IIG3p_,
				'_IIO0_1_': _IIO0_1_,
				'_IIONG_': _IIONG_,
				'_IIO1p_': _IIO1p_,
				'_IIO1_2_': _IIO1_2_,
				'_IIO2p_': _IIO2p_,
				'_IIO3p_': _IIO3p_,
				'_1si0_4_': _1si0_4_,
				'_1siII1p_': _1siII1p_,
				'_1si2_6_': _1si2_6_,
				'_1siI1p_': _1siI1p_,
				'_1si2_5_': _1si2_5_,
				'_1si0_3_': _1si0_3_,
				'_1si2_4_': _1si2_4_,
				'_1siI1psiII1p_': _1siI1psiII1p_,
				'_1si3p_': _1si3p_,
				'_1siII2p_': _1siII2p_,
				'_1si0_2_': _1si0_2_,
				'_1si3_6_': _1si3_6_,
				'_1siImII_': _1siImII_,
				'_1siGG_': _1siGG_,
				'_1si2_3_': _1si2_3_,
				'_1si3_5_': _1si3_5_,
				'_1siI2p_': _1siI2p_,
				'_1si4p_': _1si4p_,
				'_1siImmII_': _1siImmII_,
				'_1siIeII_': _1siIeII_,
				'_1si5p_': _1si5p_,
				'_1si2p_': _1si2p_,
				'_1siG2p_': _1siG2p_,
				'_2si2p_': _2si2p_,
				'_2siO2p_': _2siO2p_,
				'_2si0_4_': _2si0_4_,
				'_2siII1p_': _2siII1p_,
				'_2si2_6_': _2si2_6_,
				'_2siI1p_': _2siI1p_,
				'_2si0_3_': _2si0_3_,
				'_2si2_5_': _2si2_5_,
				'_2si2_4_': _2si2_4_,
				'_2siI1psiII1p_': _2siI1psiII1p_,
				'_2si3p_': _2si3p_,
				'_2siII2p_': _2siII2p_,
				'_2si0_2_': _2si0_2_,
				'_2si3_6_': _2si3_6_,
				'_2siImII_': _2siImII_,
				'_2siGG_': _2siGG_,
				'_2si2_3_': _2si2_3_,
				'_2si3_5_': _2si3_5_,
				'_2siI2p_': _2siI2p_,
				'_2siImmII_': _2siImmII_,
				'_2si4p_': _2si4p_,
				'_2siIeII_': _2siIeII_,
				'_2si5p_': _2si5p_,
				'_Xsi0_2_': _Xsi0_2_,
				'_Xsi2p_': _Xsi2p_,
				'_Xsi2_4_': _Xsi2_4_,
				'_XsiIeII_': _XsiIeII_,
				'_XsiImII_': _XsiImII_,
				'_XsiImmII_': _XsiImmII_,
				'_Xsi4p_': _Xsi4p_,
				'_ImmII_': _ImmII_,
				'_IeII_': _IeII_,
				'_ImII_': _ImII_,
				'_ImmeII_': _ImmeII_,
				'_ImeII_': _ImeII_,
				'_ImmmII_': _ImmmII_,
				'_IG0_1siIIG0_2_': _IG0_1siIIG0_2_,
				'_IG0_2siIIG0_1_': _IG0_2siIIG0_1_,
				'_IG0_1siIIG0_1_': _IG0_1siIIG0_1_,
				'_IGNGsIIGNG_': _IGNGsIIGNG_,
				'_IGNGsiIIG1p_': _IGNGsiIIG1p_,
				'_IG1psiIIG1p_': _IG1psiIIG1p_,
				'_IG1psiIIGNG_': _IG1psiIIGNG_,
				'_IGNGsiIIG2p_': _IGNGsiIIG2p_,
				'_IG1psiIIG2p_': _IG1psiIIG2p_,
				'_IG2psiIIG1p_': _IG2psiIIG1p_,
				'_IG2psiIIGNG_': _IG2psiIIGNG_,
				'_IG2psiIIG2p_': _IG2psiIIG2p_,
				'_IG1psiIIG3p_': _IG1psiIIG3p_,
				'_IO0_1siIIO0_2_': _IO0_1siIIO0_2_,
				'_IO0_2siIIO0_1_': _IO0_2siIIO0_1_,
				'_IO0_1siIIO0_1_': _IO0_1siIIO0_1_,
				'_IONGsIIONG_': _IONGsIIONG_,
				'_IONGsiIIO1p_': _IONGsiIIO1p_,
				'_IO1psiIIO1p_': _IO1psiIIO1p_,
				'_IO1psiIIONG_': _IO1psiIIONG_,
				'_IONGsiIIO2p_': _IONGsiIIO2p_,
				'_IO1psiIIO2p_': _IO1psiIIO2p_,
				'_IO2psiIIO1p_': _IO2psiIIO1p_,
				'_IO2psiIIONG_': _IO2psiIIONG_,
				'_IO2psiIIO2p_': _IO2psiIIO2p_,
				'_IO1psiIIO3p_': _IO1psiIIO3p_,
				'_IO0_2siIIO0_2_': _IO0_2siIIO0_2_,
				'_1__1_': _1__1_,
				'_1__0_': _1__0_,
				'_2__1_': _2__1_,
				'_0__1_': _0__1_,
				'_0__0_': _0__0_,
				'_2__0_': _2__0_,
				'_1___2_': _1___2_,
				'_2__2_': _2__2_,
				'_0__2_': _0__2_,
				'_3__1_': _3__1_,
				'_3__0_': _3__0_,
				'_1__3_': _1__3_,
				'_3__2_': _3__2_,
				'_2__3_': _2__3_,
				'_0__3_': _0__3_,
				'_4__1_': _4__1_,
				'_4__0_': _4__0_,
				'_3__3_': _3__3_,
				'_4__2_': _4__2_,
				'_5__0_': _5__0_,
				'_5__1_': _5__1_,
				'_6__0_': _6__0_,
				'_0__4_': _0__4_,
				'_1__4_': _1__4_,
				'_2__4_': _2__4_,
				'_0__5_': _0__5_,
				'_1__5_': _1__5_,
				'_0__6_': _0__6_,
				'_I1__0_': _I1__0_,
				'_I2__0_': _I2__0_,
				'_I2__1_': _I2__1_,
				'_I1__2_': _I1__2_,
				'_I0__2_': _I0__2_,
				'_I0__1_': _I0__1_,
				'_I0__0_': _I0__0_,
				'_I1__1_': _I1__1_,
				'_I2__2_': _I2__2_,
				'_S2pt00_': _S2pt00_,
				'_P2pt00_': _P2pt00_,
				'_S3pt00_': _S3pt00_,
				'_P3pt00_': _P3pt00_,
				'_S4pt00_': _S4pt00_,
				'_P4pt00_': _P4pt00_,
				'_HA1_1_': _HA1_1_,
				'_HA2_1_': _HA2_1_,
				'_PGGsi2p_': _PGGsi2p_,
				'_PGGsi3p_': _PGGsi3p_,
				'_PGGsi4p_': _PGGsi4p_,
				'_PGGsiGG_': _PGGsiGG_,
				'_PGGsiG2p_': _PGGsiG2p_,
				'_PGOsi2p_': _PGOsi2p_,
				'_PGOsi3p_': _PGOsi3p_,
				'_PGOsi4p_': _PGOsi4p_,
				'_PGOsiGG_': _PGOsiGG_,
				'_PGOsiO2p_': _PGOsiO2p_,
				'_Par_': _Par_,
				'_Impar_': _Impar_,
				'_1Xsi0_4_': _1Xsi0_4_,
				'_1XsiII1p_': _1XsiII1p_,
				'_1Xsi0_3_': _1Xsi0_3_,
				'_1Xsi2p_': _1Xsi2p_,
				'_1Xsi2_6_': _1Xsi2_6_,
				'_1Xsi2_5_': _1Xsi2_5_,
				'_1XsiI1p_': _1XsiI1p_,
				'_1Xsi2_4_': _1Xsi2_4_,
				'_1XsiPGG_': _1XsiPGG_,
				'_1Xsi0_2_': _1Xsi0_2_,
				'_1XsiGG_': _1XsiGG_,
				'_1XsiI1psiII1p_': _1XsiI1psiII1p_,
				'_1Xsi3p_': _1Xsi3p_,
				'_1XsiImII_': _1XsiImII_,
				'_1Xsi3_6_': _1Xsi3_6_,
				'_1Xsi3_5_': _1Xsi3_5_,
				'_1Xsi2_3_': _1Xsi2_3_,
				'_1XsiII2p_': _1XsiII2p_,
				'_1XsiIeII_': _1XsiIeII_,
				'_1XsiI2p_': _1XsiI2p_,
				'_1XsiImmII_': _1XsiImmII_,
				'_1XsiPGO_': _1XsiPGO_,
				'_1Xsi4p_': _1Xsi4p_,
				'_1Xsi5p_': _1Xsi5p_,
				'_X2si0_4_': _X2si0_4_,
				'_X2si2p_': _X2si2p_,
				'_X2si2_6_': _X2si2_6_,
				'_X2si2_5_': _X2si2_5_,
				'_X2siI1p_': _X2siI1p_,
				'_X2si2_4_': _X2si2_4_,
				'_X2si0_2_': _X2si0_2_,
				'_X2siGG_': _X2siGG_,
				'_X2siI1psiII1p_': _X2siI1psiII1p_,
				'_X2siPGO_': _X2siPGO_,
				'_X2si3p_': _X2si3p_,
				'_X2si3_6_': _X2si3_6_,
				'_X2siII2p_': _X2siII2p_,
				'_X2si2_3_': _X2si2_3_,
				'_X2siIeII_': _X2siIeII_,
				'_X2siI2p_': _X2siI2p_,
				'_X2siImmII_': _X2siImmII_,
				'_X2siPGG_': _X2siPGG_,
				'_X2si4p_': _X2si4p_,
				'_X2si5p_': _X2si5p_,
				'_X2si0_3_': _X2si0_3_,
				'_X2siII1p_': _X2siII1p_,
				'_X2siImII_': _X2siImII_,
				'_X2si3_5_': _X2si3_5_,
				'_12si0_4_': _12si0_4_,
				'_12siII1p_': _12siII1p_,
				'_12si2_6_': _12si2_6_,
				'_12si2p_': _12si2p_,
				'_12si2_5_': _12si2_5_,
				'_12siI1p_': _12siI1p_,
				'_12si0_3_': _12si0_3_,
				'_12si2_4_': _12si2_4_,
				'_12siI1psiII1p_': _12siI1psiII1p_,
				'_12siPGG_': _12siPGG_,
				'_12si3p_': _12si3p_,
				'_12siII2p_': _12siII2p_,
				'_12si0_2_': _12si0_2_,
				'_12si3_6_': _12si3_6_,
				'_12siImII_': _12siImII_,
				'_12siGG_': _12siGG_,
				'_12siPGO_': _12siPGO_,
				'_12siI2p_': _12siI2p_,
				'_12siImmII_': _12siImmII_,
				'_12si4p_': _12si4p_,
				'_12siIeII_': _12siIeII_,
				'_12si5p_': _12si5p_,
				'_12si2_3_': _12si2_3_,
				'_12si3_5_': _12si3_5_,
				'_1_1si0_4_': _1_1si0_4_,
				'_1_1si2p_': _1_1si2p_,
				'_1_1si2_6_': _1_1si2_6_,
				'_1_1si2_5_': _1_1si2_5_,
				'_1_1si0_3_': _1_1si0_3_,
				'_X_Xsi0_2_': _X_Xsi0_2_,
				'_1_1si2_4_': _1_1si2_4_,
				'_X_1si0_4_': _X_1si0_4_,
				'_2_2si0_4_': _2_2si0_4_,
				'_X_Xsi2p_': _X_Xsi2p_,
				'_1_1si3p_': _1_1si3p_,
				'_1_1siNGG_': _1_1siNGG_,
				'_1_1si3_6_': _1_1si3_6_,
				'_2_2si2p_': _2_2si2p_,
				'_2_2si2_6_': _2_2si2_6_,
				'_X_Xsi2_4_': _X_Xsi2_4_,
				'_X_1si2p_': _X_1si2p_,
				'_1_1si2_3_': _1_1si2_3_,
				'_X_1si2_6_': _X_1si2_6_,
				'_1_1siII2p_': _1_1siII2p_,
				'_2_2si2_5_': _2_2si2_5_,
				'_2_2si0_3_': _2_2si0_3_,
				'_X_1si2_5_': _X_1si2_5_,
				'_X_2si0_4_': _X_2si0_4_,
				'_2_2si2_4_': _2_2si2_4_,
				'_X_1si2_4_': _X_1si2_4_,
				'_1_1siGG_': _1_1siGG_,
				'_X_1siNGG_': _X_1siNGG_,
				'_X_2si0_3_': _X_2si0_3_,
				'_1_1si0_2_': _1_1si0_2_,
				'_2_2siNGG_': _2_2siNGG_,
				'_X_2si2p_': _X_2si2p_,
				'_X_2si2_6_': _X_2si2_6_,
				'_2_2si3_6_': _2_2si3_6_,
				'_X_2si2_5_': _X_2si2_5_,
				'_2_2si3_5_': _2_2si3_5_,
				'_1_1siI2p_': _1_1siI2p_,
				'_X_2siNGG_': _X_2siNGG_,
				'_2_2siII2p_': _2_2siII2p_,
				'_X_2si5p_': _X_2si5p_,
				'_2_2si2_3_': _2_2si2_3_,
				'_X_1siGG_': _X_1siGG_,
				'_X_1si2_3_': _X_1si2_3_,
				'_X_2si0_2_': _X_2si0_2_,
				'_X_1si3_6_': _X_1si3_6_,
				'_1_1si4p_': _1_1si4p_,
				'_2_2si0_2_': _2_2si0_2_,
				'_X_1si3_5_': _X_1si3_5_,
				'_X_2siII2p_': _X_2siII2p_,
				'_X_2siGG_': _X_2siGG_,
				'_X_1siI2p_': _X_1siI2p_,
				'_X_XsiI2p_': _X_XsiI2p_,
				'_X_2si3p_': _X_2si3p_,
				'_X_2si3_6_': _X_2si3_6_,
				'_X_2si3_5_': _X_2si3_5_,
				'_2_2si4p_': _2_2si4p_,
				'_X_2siI2p_': _X_2siI2p_,
				'_X_1si4p_': _X_1si4p_,
				'_1_1si5p_': _1_1si5p_,
				'_X_2si4p_': _X_2si4p_,
				'_X_Xsi4p_': _X_Xsi4p_,
				'_2_2si5p_': _2_2si5p_,
				'_X_1si5p_': _X_1si5p_,
				'_2_1si4p_': _2_1si4p_,
				'_1_2si4p_': _1_2si4p_,
				'_2_1si5p_': _2_1si5p_,
				'_1_2si5p_': _1_2si5p_,
				'_1_1si3_5_': _1_1si3_5_,
				'_X_1si0_3_': _X_1si0_3_,
				'_2_2si3p_': _2_2si3p_,
				'_X_1si0_2_': _X_1si0_2_,
				'_X_1siII2p_': _X_1siII2p_,
				'_X_2si2_4_': _X_2si2_4_,
				'_X_XsiII2p_': _X_XsiII2p_,
				'_2_2siGG_': _2_2siGG_,
				'_X_1si3p_': _X_1si3p_,
				'_2_2siI2p_': _2_2siI2p_,
				'_X_2si2_3_': _X_2si2_3_,
				'_1siPGG_': _1siPGG_,
				'_2siPGO_': _2siPGO_,
				'_1siPGO_': _1siPGO_,
				'_2siPGG_': _2siPGG_,
				'_VSG_': _VSG_,
				'_VSO_': _VSO_,
				'_VDG_': _VDG_,
				'_VSDG_': _VSDG_,
				'_VDO_': _VDO_,
				'_VDGsi4p_': _VDGsi4p_,
				'_VSDO_': _VSDO_,
				'_VDOsi4p_': _VDOsi4p_,
				'_Xsau3p_': _Xsau3p_,
				'_1sau3p_': _1sau3p_,
				'_GGsau3p_': _GGsau3p_,
				'_IXsauIIX_': _IXsauIIX_,
				'_NGGsau0_2_': _NGGsau0_2_,
				'_2sau3p_': _2sau3p_,
				'_I2psauII2p_': _I2psauII2p_,
				'_I1sauII1_': _I1sauII1_,
				'_2sau4p_': _2sau4p_,
				'_I2sauII2_': _I2sauII2_,
				'_IGGsauIIGG_': _IGGsauIIGG_,
				'_I2psau4p_': _I2psau4p_,
				'_1_1sau2_2_': _1_1sau2_2_,
				'_1_1sauX_1_': _1_1sauX_1_,
				'_X_XsauX_1_': _X_XsauX_1_,
				'_X_XsauX_2_': _X_XsauX_2_,
				'_X_1sauX_2_': _X_1sauX_2_,
				'_2_2sauX_2_': _2_2sauX_2_,
				'_I3psauII3p_': _I3psauII3p_,
				'_1sau4p_': _1sau4p_,
				'_2sauI2p_': _2sauI2p_,
				'_1sauI2p_': _1sauI2p_,
				'_Xsau0_2_': _Xsau0_2_,
				# '_SC_1_': _SC_1_,
				# '_SC_X_': _SC_X_,
				# '_SC_2_': _SC_2_,
				# '_SC_1X_': _SC_1X_,
				# '_SC_X2_': _SC_X2_,
				# '_SC_12_': _SC_12_,
				# '_SE_1_': _SE_1_,
				# '_SE_X_': _SE_X_,
				# '_SE_2_': _SE_2_,
				# '_SE_1X_': _SE_1X_,
				# '_SE_X2_': _SE_X2_,
				# '_SE_12_': _SE_12_,
				}