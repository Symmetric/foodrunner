# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recipient'
        db.create_table(u'core_recipient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location_lat', self.gf('django.db.models.fields.FloatField')()),
            ('location_lng', self.gf('django.db.models.fields.FloatField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'core', ['Recipient'])


    def backwards(self, orm):
        # Deleting model 'Recipient'
        db.delete_table(u'core_recipient')


    models = {
        u'core.donation': {
            'Meta': {'object_name': 'Donation'},
            'available_time': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'expire_time': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_lat': ('django.db.models.fields.FloatField', [], {}),
            'location_lng': ('django.db.models.fields.FloatField', [], {}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        u'core.recipient': {
            'Meta': {'object_name': 'Recipient'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_lat': ('django.db.models.fields.FloatField', [], {}),
            'location_lng': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['core']