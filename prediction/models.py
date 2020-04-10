from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from data import models as data_models


class RiskType():
    name = models.CharField(max_length=255)


class RiskLevel():
    name = models.CharField(max_length=255)


class Prediction(core_models.TimeStampedModel):

    employment = models.ForeignKey(data_models.Employment, related_name="prediction", on_delete=models.PROTECT)
    country = CountryField()
    report_date = models.DateField()
    risk_type = models.ForeignKey(RiskType, related_name="prediction", on_delete=models.PROTECT)
    risk_level = models.ForeignKey(RiskLevel, related_name="prediction", on_delete=models.PROTECT)
    description = models.TextField()
    action = models.TextField()
