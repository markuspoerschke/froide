# Generated by Django 2.1.4 on 2019-02-24 09:40

from django.db import migrations
import django_wikidata.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publicbody', '0025_remove_publicbody_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicbody',
            name='wikidata_item',
            field=django_wikidata.fields.WikidataItemField(default='', max_length=50),
        ),
    ]