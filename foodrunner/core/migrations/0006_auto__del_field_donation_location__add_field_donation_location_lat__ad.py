# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Donation.location'
        db.delete_column(u'core_donation', 'location')

        # Adding field 'Donation.location_lat'
        db.add_column(u'core_donation', 'location_lat',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Donation.location_lng'
        db.add_column(u'core_donation', 'location_lng',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Donation.location'
        raise RuntimeError("Cannot reverse this migration. 'Donation.location' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Donation.location'
        db.add_column(u'core_donation', 'location',
                      self.gf('django.db.models.fields.CharField')(max_length=1000),
                      keep_default=False)

        # Deleting field 'Donation.location_lat'
        db.delete_column(u'core_donation', 'location_lat')

        # Deleting field 'Donation.location_lng'
        db.delete_column(u'core_donation', 'location_lng')


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
        }
    }

    complete_apps = ['core']