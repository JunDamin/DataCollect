from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin
from . import models

# Register your models here.


@admin.register(models.RiskLevel)
class ItemAdmin(ImportExportMixin, admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "score", "description")


class PredictionResource(resources.ModelResource):
    class Meta:
        model = models.Prediction
        fields = (
            "id",
            "department",
            "department__name",
            "latest_prediction",
            "country",
            "country__korean",
            "report_date",
            "political_risk",
            "safety_risk",
            "disaster_risk",
            "medical_risk",
            "other_risk",
            "description",
            "action",
            "author",
            "author__first_name",
        )
        export_order = (
            "id",
            "department",
            "department__name",
            "latest_prediction",
            "country",
            "country__korean",
            "report_date",
            "political_risk",
            "safety_risk",
            "disaster_risk",
            "medical_risk",
            "other_risk",
            "description",
            "action",
            "author",
            "author__first_name",
        )


@admin.register(models.Prediction)
class PredictionAdmin(ImportExportMixin, admin.ModelAdmin):
    """ Prediction Admin Definition """

    resource_class = PredictionResource

    list_display = (
        "department",
        "country",
        "report_date",
        "latest_prediction",
        "political_risk",
        "safety_risk",
        "disaster_risk",
        "medical_risk",
        "other_risk",
        "description",
        "action",
    )

    list_filter = (
        "department",
        "political_risk",
        "safety_risk",
        "disaster_risk",
        "medical_risk",
        "other_risk",
        "country",
    )
