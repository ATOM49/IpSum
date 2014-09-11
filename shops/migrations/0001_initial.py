# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Shop'
        db.create_table(u'shops_shop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shop_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('shop_address', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('shop_category', self.gf('django.db.models.fields.CharField')(default='GS', max_length=2)),
            ('shop_location', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=20, null=True)),
            ('shop_contact_no', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('shop_email', self.gf('django.db.models.fields.EmailField')(max_length=30, null=True)),
            ('shop_info_text', self.gf('django.db.models.fields.CharField')(max_length=2048, null=True)),
            ('shop_admin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'shops', ['Shop'])

        # Adding model 'Catalog'
        db.create_table(u'shops_catalog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shops.Shop'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('price', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'shops', ['Catalog'])

        # Adding model 'ProductOffer'
        db.create_table(u'shops_productoffer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('offer_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('offer_info', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True)),
            ('points_needed', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('offer_catalog_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shops.Catalog'], null=True)),
        ))
        db.send_create_signal(u'shops', ['ProductOffer'])

        # Adding model 'ShopUserRelation'
        db.create_table(u'shops_shopuserrelation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shops.Shop'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('shop_review', self.gf('django.db.models.fields.CharField')(max_length=2048, blank=True)),
            ('loyalty_points', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('user_like', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('visited', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'shops', ['ShopUserRelation'])

        # Adding model 'ShopOffer'
        db.create_table(u'shops_shopoffer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('offer_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('offer_info', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True)),
            ('points_needed', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('offer_category', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('offer_shop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shops.Shop'], null=True)),
        ))
        db.send_create_signal(u'shops', ['ShopOffer'])

        # Adding model 'ProductUserRelation'
        db.create_table(u'shops_productuserrelation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('product_review', self.gf('django.db.models.fields.CharField')(max_length=2048)),
        ))
        db.send_create_signal(u'shops', ['ProductUserRelation'])

        # Adding model 'ShoppingCart'
        db.create_table(u'shops_shoppingcart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('shop', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['shops.Shop'], null=True)),
        ))
        db.send_create_signal(u'shops', ['ShoppingCart'])

        # Adding model 'History'
        db.create_table(u'shops_history', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('shop_user_relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shops.ShopUserRelation'])),
        ))
        db.send_create_signal(u'shops', ['History'])


    def backwards(self, orm):
        # Deleting model 'Shop'
        db.delete_table(u'shops_shop')

        # Deleting model 'Catalog'
        db.delete_table(u'shops_catalog')

        # Deleting model 'ProductOffer'
        db.delete_table(u'shops_productoffer')

        # Deleting model 'ShopUserRelation'
        db.delete_table(u'shops_shopuserrelation')

        # Deleting model 'ShopOffer'
        db.delete_table(u'shops_shopoffer')

        # Deleting model 'ProductUserRelation'
        db.delete_table(u'shops_productuserrelation')

        # Deleting model 'ShoppingCart'
        db.delete_table(u'shops_shoppingcart')

        # Deleting model 'History'
        db.delete_table(u'shops_history')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'model_number': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'mrp': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'product_category': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'product_type': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'shops.catalog': {
            'Meta': {'object_name': 'Catalog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shops.Shop']"})
        },
        u'shops.history': {
            'Meta': {'object_name': 'History'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"}),
            'shop_user_relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shops.ShopUserRelation']"})
        },
        u'shops.productoffer': {
            'Meta': {'object_name': 'ProductOffer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offer_catalog_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shops.Catalog']", 'null': 'True'}),
            'offer_info': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'offer_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'points_needed': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'shops.productuserrelation': {
            'Meta': {'object_name': 'ProductUserRelation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"}),
            'product_review': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'shops.shop': {
            'Meta': {'object_name': 'Shop'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shop_address': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'shop_admin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'shop_category': ('django.db.models.fields.CharField', [], {'default': "'GS'", 'max_length': '2'}),
            'shop_contact_no': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'shop_email': ('django.db.models.fields.EmailField', [], {'max_length': '30', 'null': 'True'}),
            'shop_info_text': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True'}),
            'shop_location': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '20', 'null': 'True'}),
            'shop_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'shops.shopoffer': {
            'Meta': {'object_name': 'ShopOffer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offer_category': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'offer_info': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'offer_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'offer_shop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shops.Shop']", 'null': 'True'}),
            'points_needed': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'shops.shoppingcart': {
            'Meta': {'object_name': 'ShoppingCart'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['shops.Shop']", 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'shops.shopuserrelation': {
            'Meta': {'object_name': 'ShopUserRelation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loyalty_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shops.Shop']"}),
            'shop_review': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_like': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'visited': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['shops']