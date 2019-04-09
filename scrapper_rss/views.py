import django_filters
from rest_framework import viewsets, filters
from rest_framework.response import Response

from scrapper_rss.models import RSSData
from scrapper_rss.serializer import RSSDataSerializer


class RssViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows data to be displayed
    """
    queryset = RSSData.objects.filter(type__active=True)
    serializer_class = RSSDataSerializer
    filter_backends = (
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        django_filters.OrderingFilter
    )
    filterset_fields = ('date', 'type__type')
    ordering = '-date,-created_at'

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = RSSDataSerializer(queryset, many=True)
        return Response(serializer.data)
