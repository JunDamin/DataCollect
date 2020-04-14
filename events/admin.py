from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin
from . import models

# Register your models here.


@admin.register(models.EventType)
class ItemAdmin(ImportExportMixin, admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "description")


class EventResource(resources.ModelResource):
    class Meta:
        model = models.Event
        fields = (
            "id",
            "title",
            "country",
            "country__korean",
            "event_type",
            "event_type__name",
            "start_date",
            "is_single",
            "end_date",
            "description",
            "author",
            "author__first_name",
            "department",
            "department__name",
        )
        export_order = (
            "id",
            "title",
            "country",
            "country__korean",
            "event_type",
            "event_type__name",
            "start_date",
            "is_single",
            "end_date",
            "description",
            "author",
            "author__first_name",
            "department",
            "department__name",
        )


@admin.register(models.Event)
class EventAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = EventResource

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
