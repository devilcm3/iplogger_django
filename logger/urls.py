from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'add_torrent/$','logger.views.add_torrent'),
	url(r'add_peer/$','logger.views.add_peer'),
)