from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


# Collect Master Data Class


class Country(models.Model):

    """ Define countries that use """

    code = CountryField()
    korean = models.CharField(max_length=255)

    def __str__(self):
        return self.code.name

    def name(self):
        return self.korean


class Employment(core_models.TimeStampedModel):

    """ Define employment ID """

    name = models.CharField(max_length=255)
    koica_code = models.CharField(max_length=255)
    location = CountryField()

    def __str__(self):
        return self.name


class EmploymentDetail(core_models.TimeStampedModel):

    """ Define Employment details.
    When they update, actually, they create detail. """

    employment = models.ForeignKey(
        Employment, related_name="employment_detail", on_delete=models.PROTECT
    )
    address = models.TextField()
    countries = models.ManyToManyField(
        Country, related_name="employment_detail", blank=True
    )
    description = models.TextField()
    antecedents = models.ManyToManyField(
        Employment, related_name="antecedents", blank=True
    )
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.employment.name + " detail"


class Region(models.Model):
    name = models.CharField(max_length=255)
    countries = models.ManyToManyField(Country, related_name="regions", blank=True,)

    def __str__(self):
        return self.name
