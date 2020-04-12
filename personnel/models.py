from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models
from data import models as data_models

# Create your models here.


class PersonnelType(core_models.TimeStampedModel):

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    the_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PersonnelInfo(core_models.TimeStampedModel):

    personnel = models.ForeignKey(
        "PersonnelType", related_name="info", on_delete=models.PROTECT
    )
    number = models.IntegerField()
    report = models.ForeignKey(
        "PersonnelReport", related_name="info", on_delete=models.CASCADE
    )


class PersonnelReport(core_models.TimeStampedModel):

    department = models.ForeignKey(
        data_models.Department,
        related_name="personnel",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    report_date = models.DateField()
    country = CountryField()
    author = models.ForeignKey(
        user_models.User,
        related_name="personnel",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def sum(self):
        return self.info.all().aggregate(models.Sum("number")).get("number__sum")
