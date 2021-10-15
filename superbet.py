# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.http.request import Request
from datetime import datetime


class FtgSpider(scrapy.Spider):
	name = 'superbet'
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
				name = x['mn']
				name = name.split('·')
				home = name[0].strip()
				away = name[1].strip()
			except:
				pass
			
			try:
				cleague = x["tn2"]
				cleague = cleague.split('|', 1)[1]
				cleague = cleague.split('|', 1)[0]
				cleague = cleague.split(' - ')
				country = cleague[0].strip()
				league = cleague[1].strip()
			except:
				pass
			dt = x["mld"]
			s_id = x["_id"]
			ci = x["ci"]
			li = x["ti"]
			hi = x["ti1"]
			ai = x["ti2"]
			odds = x['odds']
			

			_1_= None
			for x in odds:
				groupId = x['groupId']
				oc = x.get('oc')
				groupId_oc = str(groupId) + "#" + str(oc)
				if groupId_oc == "3#11":
					_1_ = x['ov']
				else:
					if groupId_oc == "547#1":
						_1_ = x['ov']


			_X_= None
			for x in odds:
				groupId = x['groupId']
				oc = x.get('oc')
				groupId_oc = str(groupId) + "#" + str(oc)
				if groupId_oc == "3#10":
					_X_ = x['ov']
				else:
					if groupId_oc == "547#0":
						_X_ = x['ov']

			_2_= None
			for x in odds:
				groupId = x['groupId']
				oc = x.get('oc')
				groupId_oc = str(groupId) + "#" + str(oc)
				if groupId_oc == "3#12":
					_2_ = x['ov']
				else:
					if groupId_oc == "547#2":
						_2_ = x['ov']

			_0_2_ = None
			for x in odds:
				groupId = x['groupId']
				oc = x.get('oc')
				groupId_oc = str(groupId) + "#" + str(oc)
				if groupId_oc == "18#0-2":
					_0_2_ = x['ov']
				else:
					if groupId_oc == "200734#-":
						osbv = x.get('osbv')
						groupId_oc_osbv = groupId_oc + "#" + str(osbv)
						if groupId_oc_osbv == "200734#-#2.5":
							_0_2_ = x['ov']

			_3p_ = None
			for x in odds:
				groupId = x['groupId']
				oc = x.get('oc')
				groupId_oc = str(groupId) + "#" + str(oc)
				if groupId_oc == "18#3+":
					_3p_ = x['ov']
				else:
					if groupId_oc == "200734#+":
						osbv = x.get('osbv')
						groupId_oc_osbv = groupId_oc + "#" + str(osbv)
						if groupId_oc_osbv == "200734#+#2.5":
							_3p_ = x['ov']

			yield {
				's_id': s_id,				              
				'country': country,
				'ci': ci,
				'league': league,
				'li': li,
				'home': home,
				'hi': hi,
				'away': away,
				'ai': ai,			
				'dt': dt,
				'_1_': _1_,
				'_X_': _X_,
				'_2_': _2_,
				'_0_2_': _0_2_,
				'_3p_': _3p_,}
