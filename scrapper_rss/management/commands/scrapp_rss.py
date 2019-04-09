import datetime
import logging
import feedparser

from dateutil import parser
from django.core.management.base import BaseCommand

from django.conf import settings
from django.db import transaction

from scrapper_rss.models import RSSTypes, RSSData


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    default_types_qs = RSSTypes.objects.filter(active=True)

    def handle(self, *args, **options):
        erorr_counter = 0

        while erorr_counter < 10:
            now = datetime.datetime.now()
            last_fetched_before = now - settings.FETCHER_DELAY
            types_qs = self.default_types_qs.exclude(
                last_fetch__gt=last_fetched_before
            ).select_for_update(skip_locked=True)

            with transaction.atomic():
                rss_type = types_qs.first()
                if not rss_type:
                    return

                feed = feedparser.parse(rss_type.url)
                if not hasattr(feed, 'status') or feed.status != 200 or not feed.entries:
                    logging.getLogger(__name__).error(
                        'No response for type %s url %s, status %s',
                        rss_type.type,
                        rss_type.url,
                        feed.status,
                    )
                    erorr_counter += 1
                    continue

                data_to_save = []
                for entry in feed.entries:
                    time = parser.parse(entry['updated'])
                    if rss_type.last_fetch and time <= rss_type.last_fetch:
                        break
                    data_to_save.append(RSSData(
                        date=time.date(),
                        type=rss_type,
                        data=entry,
                    ))
                RSSData.objects.bulk_create(data_to_save)
                rss_type.last_fetch = parser.parse(now)
                rss_type.save()
            erorr_counter = 0
