from rest_framework import serializers

from scrapper_rss.models import RSSData


class RSSDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RSSData
        fields = ('id', 'created_at', 'date', 'currency', 'title', 'link', 'summary', 'updated', 'exchange_rate')
