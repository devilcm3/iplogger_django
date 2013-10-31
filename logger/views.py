from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from logger.models import *

@csrf_exempt
def add_torrent(request):
	if request.method == 'POST':
		params = request.POST
		if not Torrent.objects.filter(torrent_hash = params['torrent_hash']):
			t = Torrent(
				torrent_hash= params['torrent_hash'], 
				title 		= params['title'], 
				category	= ( params['filename'] if 'filename' in params else ''),
				published	= ( params['published'] if 'published' in params else None),
				spidered	= ( params['spidered'] if 'spidered' in params else None),
			)
			t.save()
	return HttpResponse(status=200)

@csrf_exempt
def add_peer(request):
	if request.method == 'POST':
		params = request.POST

		p = Peer()
		if Peer.objects.filter(ip_address = params['ip_address']):
			p = Peer.objects.get(ip_address = params['ip_address'])

		else:
			p = Peer(
				ip_address	= params['ip_address'],
				country 	= ( params['country'] if 'country' in params else '' ),
				client_type = ( params['client_type'] if 'client_type' in params else '' ),
			)
			p.save()

		if 'torrent_hash' in params:
			t = Torrent.objects.get(torrent_hash = params['torrent_hash'])

			a = Activity()
			if Activity.objects.filter(peer = p, torrent = t):
				pass
			else:
				a = Activity(
					peer = p,
					torrent = t,
					download_speed = params['download_speed'],
					upload_speed = params['upload_speed']
					)
			a.save()
	return HttpResponse(status=200)




