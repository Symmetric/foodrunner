# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Donation.highlighted'
        db.delete_column(u'core_donation', 'highlighted')

        # Deleting field 'Donation.owner'
        db.delete_column(u'core_donation', 'owner_id')


    def backwards(self, orm):
        # Adding field 'Donation.highlighted'
        db.add_column(u'core_donation', 'highlighted',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)

        # Adding field 'Donation.owner'
        db.add_column(u'core_donation', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='donations', null=True, to=orm['auth.User']),
                      keep_default=False)


    models = {
        u'core.donation': {
            'Meta': {'object_name': 'Donation'},
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