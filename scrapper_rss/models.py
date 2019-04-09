from django.contrib.postgres.fields import JSONField
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class RSSTypes(BaseModel):
    last_fetch = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)
    type = models.CharField(max_length=100)
    url = models.TextField()


class RSSData(BaseModel):
    date = models.DateField()
    type = models.ForeignKey(
        'RSSTypes',
        on_delete=models.CASCADE,
    )
    data = JSONField()

    @property
    def currency(self):
        return self.type.type

    @property
    def title(self):
        return self.data['title']

    @property
    def link(self):
        return self.data['link']

    @property
    def summary(self):
        return self.data['summary']

    @property
    def updated(self):
        return self.data['updated']

    @property
    def exchange_rate(self):
        return self.data['cb_exchangerate']