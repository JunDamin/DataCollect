from django.db import models
from django.urls import reverse
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
    score = models.IntegerField(null=True, blank=True)
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
    country = models.ForeignKey(
        data_models.Country, related_name="prediction", on_delete=models.PROTECT
    )
    report_date = models.DateField()

    political_risk = models.ForeignKey(
        RiskLevel,
        verbose_name="정정불안",
        related_name="prediction_political",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    safety_risk = models.ForeignKey(
        RiskLevel,
        verbose_name="치안",
        related_name="prediction_safety",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    disaster_risk = models.ForeignKey(
        RiskLevel,
        verbose_name="자연재해",
        related_name="prediction_disaster",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    medical_risk = models.ForeignKey(
        RiskLevel,
        verbose_name="질병",
        related_name="prediction_medical",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    other_risk = models.ForeignKey(
        RiskLevel,
        verbose_name="기타",
        related_name="prediction_others",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
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

    latest_prediction = models.OneToOneField(
        data_models.Department,
        on_delete=models.PROTECT,
        related_name="latest_prediction",
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
