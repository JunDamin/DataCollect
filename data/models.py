from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


# Create your models here.

class Country():
    code = CountryField()

    def __str__(self):
        return self.code.name


class Employment():

    name = models.CharField(max_length=255)
    koica_code = models.CharField(max_length=255)
    location = models.ForeignKey(Country, related_name='location', on_delete=models.PROTECT)
    address = models.TextField()
    countries = models.ManyToManyField("Country", related_name="countries", blank=True)


class Region():
    name = models.CharField(max_length=255)
    countries = models.ManyToManyField("Country", related_name="countries", blank=True)
