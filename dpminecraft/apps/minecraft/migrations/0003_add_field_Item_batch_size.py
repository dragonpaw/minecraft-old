# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.batch_size'
        db.add_column(u'minecraft_item', 'batch_size',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Item.batch_size'
        db.delete_column(u'minecraft_item', 'batch_size')


    models = {
        u'minecraft.ingredient': {
            'Meta': {'ordering': "('makes', 'item')", 'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'makes'", 'to': u"orm['minecraft.Item']"}),
            'makes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['minecraft.Item']"}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        u'minecraft.item': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Item'},
            'batch_size': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['minecraft.Item']", 'through': u"orm['minecraft.Ingredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['minecraft']