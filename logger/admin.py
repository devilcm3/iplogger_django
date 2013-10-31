from django.contrib import admin
from logger.models import *

class TorrentAdmin(admin.ModelAdmin):
	list_display = ('torrent_hash','title','category','filename','published','spidered')

class PeerAdmin(admin.ModelAdmin):
	list_display = ('ip_address','country','client_type','host')
	
class ActivityAdmin(admin.ModelAdmin):
	list_display= ('torrent','peer','flags','downloaded','download_speed','upload_speed')

admin.site.register(Torrent, TorrentAdmin)
admin.site.register(Peer, PeerAdmin)
admin.site.register(Activity, ActivityAdmin)
