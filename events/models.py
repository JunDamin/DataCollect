from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
# Create your models here.


class EventType():
    name = models.CharField(max_length=255)
    description = models.TextField()


class Event(core_models.TimeStampedModel):

    country = CountryField()
    event_type = models.ForeignKey(EventType, related_name="events", on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    description = models.TextField()
