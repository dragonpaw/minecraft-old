# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'minecraft_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal(u'minecraft', ['Item'])

        # Adding model 'Ingredient'
        db.create_table(u'minecraft_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('makes', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['minecraft.Item'])),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='makes', to=orm['minecraft.Item'])),
        ))
        db.send_create_signal(u'minecraft', ['Ingredient'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'minecraft_item')

        # Deleting model 'Ingredient'
        db.delete_table(u'minecraft_ingredient')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['minecraft.Item']", 'through': u"orm['minecraft.Ingredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['minecraft']