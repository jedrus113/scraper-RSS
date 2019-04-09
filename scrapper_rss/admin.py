from django.contrib import admin

from scrapper_rss.models import RSSTypes, RSSData


admin.site.register(RSSTypes, admin.ModelAdmin)
admin.site.register(RSSData, admin.ModelAdmin)
