# -*- coding: utf-8 -*-
import datetime
from django.db import models

from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Suivi.etat'
        db.delete_column(u'base_suivi', 'etat_id')

        # Adding field 'Suivi.category'
        db.add_column(u'base_suivi', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='suivi-category', to=orm['base.Categorie']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Suivi.etat'
        db.add_column(u'base_suivi', 'etat',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='suivi-etat', to=orm['base.Etat']),
                      keep_default=False)

        # Deleting field 'Suivi.category'
        db.delete_column(u'base_suivi', 'category_id')


    models = {
        u'base.accompagnement': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Accompagnement'},
            'couleur': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'accompagnement-couleur'", 'null': 'True', 'to': u"orm['base.Couleur']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'base.categorie': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Categorie'},
            'couleur': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'categorie-couleur'", 'null': 'True', 'to': u"orm['base.Couleur']"}),
            'disable_surtaxe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'made_in_kitchen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'priorite': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'surtaxable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vat_onsite': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'categorie-vat-onsite'", 'null': 'True', 'to': u"orm['base.VAT']"}),
            'vat_takeaway': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'categorie-vat-takeaway'", 'null': 'True', 'to': u"orm['base.VAT']"})
        },
        u'base.couleur': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Couleur'},
            'blue': ('django.db.models.fields.PositiveIntegerField', [], {'default': '255'}),
            'green': ('django.db.models.fields.PositiveIntegerField', [], {'default': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'red': ('django.db.models.fields.PositiveIntegerField', [], {'default': '255'})
        },
        u'base.cuisson': {
            'Meta': {'object_name': 'Cuisson'},
            'couleur': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cuisson-couleur'", 'null': 'True', 'to': u"orm['base.Couleur']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'nom_facture': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'priorite': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'base.etat': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Etat'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'priorite': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'base.facture': {
            'Meta': {'object_name': 'Facture'},
            'couverts': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'etats': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'le suivi'", 'symmetrical': 'False', 'to': u"orm['base.Suivi']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'onsite': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'paiements': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'les paiements'", 'symmetrical': 'False', 'to': u"orm['base.Paiement']"}),
            'produits': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'les produits vendus'", 'symmetrical': 'False', 'to': u"orm['base.ProduitVendu']"}),
            'restant_a_payer': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'saved_in_stats': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'table': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'facture-table'", 'null': 'True', 'to': u"orm['base.Table']"}),
            'total_ttc': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'vats': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'vat total for each vat on a bill'", 'symmetrical': 'False', 'to': u"orm['base.VATOnBill']"})
        },
        u'base.log': {
            'Meta': {'object_name': 'Log'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'log-logtype'", 'to': u"orm['base.LogType']"})
        },
        u'base.logtype': {
            'Meta': {'ordering': "['nom']", 'object_name': 'LogType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'base.paiement': {
            'Meta': {'object_name': 'Paiement'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'montant': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'nb_tickets': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'paiement-type'", 'to': u"orm['base.PaiementType']"}),
            'valeur_unitaire': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '9', 'decimal_places': '2'})
        },
        u'base.paiementtype': {
            'Meta': {'ordering': "['nom']", 'object_name': 'PaiementType'},
            'fixed_value': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'base.printer': {
            'Meta': {'object_name': 'Printer'},
            'billing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'footer': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'header': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kitchen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manager': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '80'})
        },
        u'base.produit': {
            'Meta': {'ordering': "('categorie', 'nom')", 'object_name': 'Produit'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'produit-categorie'", 'to': u"orm['base.Categorie']"}),
            'categories_ok': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['base.Categorie']", 'symmetrical': 'False'}),
            'choix_accompagnement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'choix_cuisson': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'choix_sauce': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'nom_facture': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'prix': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'produits_ok': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'produits_ok_rel_+'", 'to': u"orm['base.Produit']"})
        },
        u'base.produitvendu': {
            'Meta': {'ordering': "('produit',)", 'object_name': 'ProduitVendu'},
            'accompagnement': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'produitvendu-accompagnement'", 'null': 'True', 'to': u"orm['base.Accompagnement']"}),
            'contient': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'contient_rel_+'", 'to': u"orm['base.ProduitVendu']"}),
            'cuisson': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'produitvendu-cuisson'", 'null': 'True', 'to': u"orm['base.Cuisson']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'made_with': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'produit-kitchen'", 'null': 'True', 'to': u"orm['base.Categorie']"}),
            'prix': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'produit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'produitvendu-produit'", 'to': u"orm['base.Produit']"}),
            'sauce': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'produitvendu-sauce'", 'null': 'True', 'to': u"orm['base.Sauce']"}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'base.sauce': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Sauce'},
            'couleur': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sauce-couleur'", 'null': 'True', 'to': u"orm['base.Couleur']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'base.statsjourcategorie': {
            'Meta': {'object_name': 'StatsJourCategorie'},
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'statsjour-categorie'", 'null': 'True', 'to': u"orm['base.Categorie']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nb': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'valeur': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'})
        },
        u'base.statsjourgeneral': {
            'Meta': {'object_name': 'StatsJourGeneral'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'statsjour-logtype'", 'null': 'True', 'to': u"orm['base.LogType']"}),
            'valeur': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'})
        },
        u'base.statsjourpaiement': {
            'Meta': {'object_name': 'StatsJourPaiement'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nb': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'paiement': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'statsjour-paiement'", 'null': 'True', 'to': u"orm['base.PaiementType']"}),
            'valeur': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'})
        },
        u'base.statsjourproduit': {
            'Meta': {'object_name': 'StatsJourProduit'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nb': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'produit': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'statsjour-produit'", 'null': 'True', 'to': u"orm['base.Produit']"}),
            'valeur': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'})
        },
        u'base.suivi': {
            'Meta': {'object_name': 'Suivi'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'suivi-category'", 'to': u"orm['base.Categorie']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'facture': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'suivi-facture'", 'to': u"orm['base.Facture']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'base.table': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Table'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'table-zone'", 'to': u"orm['base.Zone']"})
        },
        u'base.vat': {
            'Meta': {'ordering': "['name']", 'object_name': 'VAT'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'tax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '2'}),
            'value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '4'})
        },
        u'base.vatonbill': {
            'Meta': {'object_name': 'VATOnBill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'vat': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bill-vat'", 'to': u"orm['base.VAT']"})
        },
        u'base.zone': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Zone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'prix_surtaxe': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '2'}),
            'surtaxe': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['base']
