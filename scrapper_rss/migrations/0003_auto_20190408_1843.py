# Generated by Django 2.2 on 2019-04-08 18:43

from django.db import migrations


def setup_rss(apps, schema_editor):
    url = 'https://www.ecb.europa.eu/rss/fxref-{currency}.html'
    RSSTypes = apps.get_model('scrapper_rss', 'RSSTypes')
    RSSTypes.objects.bulk_create([
        RSSTypes(
            type=currency,
            url=url.format(currency=currency)
        ) for currency in {'pln', 'nok', 'usd'}
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper_rss', '0002_auto_20190408_1843'),
    ]

    operations = [
        migrations.RunPython(setup_rss),
    ]
