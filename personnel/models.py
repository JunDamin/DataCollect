from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from data import models as data_models

# Create your models here.


class PersonnelType(core_models.TimeStampedModel):

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    the_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PersonnelInfo(core_models.TimeStampedModel):

    employment = models.ForeignKey(data_models.Employment, related_name="personnel_info", on_delete=models.PROTECT)
    personnel = models.ForeignKey(PersonnelType, related_name="personnel_info", on_delete=models.PROTECT)
    number = models.IntegerField()
    country = CountryField()
    report_date = models.DateField()
    