from django.contrib import admin
from import_export.admin import ImportExportMixin
from . import models

# Register your models here.


@admin.register(models.RiskType, models.RiskLevel)
class ItemAdmin(ImportExportMixin, admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "description")


@admin.register(models.Prediction)
class ItemAdmin(ImportExportMixin, admin.ModelAdmin):

    """ Prediction Admin Definition """

    list_display = (
        "employment",
        "country",
        "report_date",
        "risk_type",
        "risk_level",
        "description",
        "action",
    )

    list_filter = (
        "employment",
        "risk_type",
        "risk_level",
        "country",
    )
