# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Peer'
        db.create_table(u'logger_peer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip_address', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('client_type', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
        ))
        db.send_create_signal(u'logger', ['Peer'])

        # Adding model 'Torrent'
        db.create_table(u'logger_torrent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('torrent_hash', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('published', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('spidered', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'logger', ['Torrent'])

        # Adding model 'Activity'
        db.create_table(u'logger_activity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('torrent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['logger.Torrent'])),
            ('peer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['logger.Peer'])),
            ('download_speed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('upload_speed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'logger', ['Activity'])


    def backwards(self, orm):
        # Deleting model 'Peer'
        db.delete_table(u'logger_peer')

        # Deleting model 'Torrent'
        db.delete_table(u'logger_torrent')

        # Deleting model 'Activity'
        db.delete_table(u'logger_activity')


    models = {
        u'logger.activity': {
            'Meta': {'object_name': 'Activity'},
            'download_speed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'peer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logger.Peer']"}),
            'torrent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['logger.Torrent']"}),
            'upload_speed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'logger.peer': {
            'Meta': {'object_name': 'Peer'},
            'client_type': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'logger.torrent': {
            'Meta': {'object_name': 'Torrent'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'peers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['logger.Peer']", 'through': u"orm['logger.Activity']", 'symmetrical': 'False'}),
            'published': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'spidered': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'torrent_hash': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['logger']