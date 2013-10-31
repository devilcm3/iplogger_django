import re
import requests
import simplejson as json
import threading
from datetime import *
from logger.models import Torrent


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

		for tor in tor_list:
			if tor[21] == "Downloading":
				s.get(url,params={'token':token, 'action':'removedata', 'hash':tor[0]})



