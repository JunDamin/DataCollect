from datetime import datetime
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models
from data import models as data_models

# Create your models here.


class EventType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Event(core_models.TimeStampedModel):

    title = models.CharField(max_length=255)
    country = CountryField()
    event_type = models.ForeignKey(
        EventType, related_name="events", on_delete=models.PROTECT
    )
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    author = models.ForeignKey(
        user_models.User,
        related_name="events",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    department = models.ForeignKey(
        data_models.Department,
        related_name="events",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def get_absolute_url(self):
        return reverse("events:detail", kwargs={"pk": self.pk})
