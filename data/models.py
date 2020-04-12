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


class Department(core_models.TimeStampedModel):

    """ Define department ID """

    name = models.CharField(max_length=255)
    koica_code = models.CharField(max_length=255)
    location = CountryField()
    is_active = models.BooleanField(verbose_name="Active", default=True)

    def __str__(self):
        return self.name

    def get_latest_prediction(self):
        print(self.prediction.filter().order_by("-created"))
        if self.prediction.filter().order_by("-created"):
            print(self.prediction.filter().order_by("-created")[0])
            return self.prediction.filter().order_by("-created")[0]
        else:
            return None

    def get_latest_personnel_report(self):
        print(self.personnel.filter().order_by("-created"))
        if self.personnel.filter().order_by("-created"):
            return self.personnel.filter().order_by("-created")[0]
        else:
            return None


class DepartmentDetail(core_models.TimeStampedModel):

    """ Define Department details.
    When they update, actually, they create detail. """

    class Meta:
        verbose_name = "Department detail"

    department = models.ForeignKey(
        Department, related_name="department_detail", on_delete=models.PROTECT
    )
    address = models.TextField()
    countries = models.ManyToManyField(
        Country, related_name="department_detail", blank=True
    )
    description = models.TextField()
    antecedents = models.ManyToManyField(
        Department, related_name="antecedents", blank=True
    )
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.department.name + " detail"


class Region(models.Model):
    name = models.CharField(max_length=255)
    countries = models.ManyToManyField(Country, related_name="regions", blank=True,)

    def __str__(self):
        return self.name
