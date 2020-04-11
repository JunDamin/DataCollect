from django.contrib import admin
from import_export.admin import ImportExportMixin
from . import models

# Register your models here.


@admin.register(models.EventType)
class ItemAdmin(ImportExportMixin, admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "description")


@admin.register(models.Event)
class EventAdmin(ImportExportMixin, admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = (
        "title",
        "country",
        "event_type",
    )

    list_filter = (
        "event_type",
        "country",
    )
