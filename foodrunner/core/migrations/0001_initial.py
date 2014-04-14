# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pickup'
        db.create_table(u'core_pickup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('contact_number', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('available_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('expire_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'core', ['Pickup'])


    def backwards(self, orm):
        # Deleting model 'Pickup'
        db.delete_table(u'core_pickup')


    models = {
        u'core.pickup': {
            'Meta': {'object_name': 'Pickup'},
            'available_time': ('django.db.models.fields.DateTimeField', [], {}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'expire_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['core']