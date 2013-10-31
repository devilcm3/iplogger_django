import re
import requests
import simplejson as json
import threading
import time


from django.core.management.base import BaseCommand,CommandError

class Command(BaseCommand):

	def handle(self, *args, **options):
		url = "http://admin:admin@localhost:55555/gui/"
		django_url = "http://127.0.0.1:8000/logger/"

		#start a session
		s = requests.Session()

		#get token
		req = s.get(url+"token.html").text
		token = re.search(r"[\w\-\_]{64}",req).group(0)

		#get torrent list
		req =  s.get(url,params={'token':token,'list':1})
		req = json.loads(req.text)
		tor_list = req['torrents']

		for i in tor_list:
			if i[21] == "Downloading":
				t = {}
				t['torrent_hash'] = i[0]
				t['title'] = i[2]

				req = requests.post(django_url + 'add_torrent/', data=t)

				req = s.get(url,params={'token':token, 'action':'getpeers', 'hash':i[0]}).text

				req = json.loads(req)
				if req['peers'][1]:
					count = 0
					for peer in req['peers'][1]:
							p = {}
							p['torrent_hash']		= t['torrent_hash']
							p['ip_address'] 		= peer[1]
							p['host']				= peer[2]
							p['port']				= peer[4]
							p['client_type']		= peer[5]
							p['flags']				= peer[6]
							p['percent_complete']	= peer[7]
							p['download_speed']		= peer[8]
							p['upload_speed']		= peer[9]
							p['waited']				= peer[12]
							p['downloaded']			= peer[14]
							p['inactive']			= peer[20]
							p['relevance']			= peer[21]

							requests.post(django_url + 'add_peer/', data=p)
