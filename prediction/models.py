from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models
from data import models as data_models
from users import models as user_models


class RiskType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class RiskLevel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Prediction(core_models.TimeStampedModel):

    department = models.ForeignKey(
        data_models.Department,
        related_name="prediction",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    country = CountryField()
    report_date = models.DateField()

    risk_type = models.ForeignKey(
        RiskType, related_name="prediction", on_delete=models.PROTECT
    )
    risk_level = models.ForeignKey(
        RiskLevel, related_name="prediction", on_delete=models.PROTECT
    )
    description = models.TextField()
    action = models.TextField()

    author = models.ForeignKey(
        user_models.User,
        related_name="prediction",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def get_absolute_url(self):
        return reverse("prediction:detail", kwargs={"pk": self.pk})

    def get_fields(self):
        return [
            (field, field.value_to_string(self))
            for field in Prediction._meta.fields
            if field.name
            in [
                "country",
                "report_date",
                "risk_type",
                "risk_level",
                "description",
                "action",
                "author",
            ]
        ]
