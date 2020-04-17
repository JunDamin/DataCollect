from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin
from . import models

# Register your models here.


@admin.register(models.RiskType, models.RiskLevel)
class ItemAdmin(ImportExportMixin, admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "description")


class PredictionResource(resources.ModelResource):
    class Meta:
        model = models.Prediction
        fields = (
            "id",
            "department",
            "department__name",
            "latest_report",
            "country",
            "country__korean",
            "report_date",
            "risk_type",
            "risk_type__name",
            "risk_level",
            "risk_level__name",
            "description",
            "action",
            "author",
            "author__first_name",
        )
        export_order = (
            "id",
            "department",
            "department__name",
            "latest_report",
            "country",
            "country__korean",
            "report_date",
            "risk_type",
            "risk_type__name",
            "risk_level",
            "risk_level__name",
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
        "risk_type",
        "risk_level",
        "description",
        "action",
    )

    list_filter = (
        "department",
        "risk_type",
        "risk_level",
        "country",
    )
