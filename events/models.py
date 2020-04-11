from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# Create your models here.


class EventType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Event(core_models.TimeStampedModel):

    name = models.CharField(max_length=255)
    country = CountryField()
    event_type = models.ForeignKey(
        EventType, related_name="events", on_delete=models.PROTECT
    )
    description = models.TextField()
