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
