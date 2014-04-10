# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Pickup.available_time'
        db.alter_column(u'core_pickup', 'available_time', self.gf('django.db.models.fields.CharField')(max_length=1000))

        # Changing field 'Pickup.expire_time'
        db.alter_column(u'core_pickup', 'expire_time', self.gf('django.db.models.fields.CharField')(max_length=1000))

    def backwards(self, orm):

        # Changing field 'Pickup.available_time'
        db.alter_column(u'core_pickup', 'available_time', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Pickup.expire_time'
        db.alter_column(u'core_pickup', 'expire_time', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'core.pickup': {
            'Meta': {'object_name': 'Pickup'},
            'available_time': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'expire_time': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['core']