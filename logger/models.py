from django.db import models

class Peer(models.Model):
	ip_address = models.CharField(max_length=64)
	country = models.CharField(max_length=64, blank=True)
	client_type = models.CharField(max_length=64, blank=True)

	def __unicode__(self):
		return self.ip_address

class Torrent(models.Model):
	torrent_hash = models.CharField(max_length=250)
	title = models.CharField(max_length=250)
	category = models.CharField(max_length=250, blank=True)
	filename = models.CharField(max_length=250, blank=True)
	published = models.DateField(blank=True, null=True)
	spidered = models.DateTimeField(blank=True, null=True)
	peers = models.ManyToManyField(Peer, through='Activity')

	def __unicode__(self):
		return self.title

class Activity(models.Model):
	torrent = models.ForeignKey(Torrent)
	peer = models.ForeignKey(Peer)
	download_speed = models.IntegerField(blank=True, null=True)
	upload_speed = models.IntegerField(blank=True, null=True)

	def __unicode__(self):
		return self.torrent.title + ' : ' + self.peer.ip_address
