from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin
from . import models


@admin.register(models.PersonnelType)
class PersonnelTypeAdmin(ImportExportMixin, admin.ModelAdmin):
    fieldsets = (("Basic Info", {"fields": ("name", "category", "the_type",)}),)

    list_display = (
        "name",
        "category",
        "the_type",
    )

    list_filter = (
        "name",
        "category",
        "the_type",
    )


@admin.register(models.PersonnelInfo)
class PersonnelInfoAdmin(ImportExportMixin, admin.ModelAdmin):
    fieldsets = (("Basic Info", {"fields": ("personnel_type", "number", "report",)},),)

    list_display = (
        "personnel_type",
        "number",
        "report",
    )

    list_filter = (
        "personnel_type",
        "number",
        "report",
    )


class PersonnelInfoInline(admin.TabularInline):
    model = models.PersonnelInfo
    extra = 0


class PersonnelReportResource(resources.ModelResource):
    class Meta:
        model = models.PersonnelReport
        fields = (
            [
                "id",
                "department",
                "department__name",
                "report_date",
                "author",
                "author__first_name",
                "country",
                "country__korean",
            ]
            + models.PersonnelReport.TOTAL_LIST
            + ["description"]
        )
        export_order = (
            [
                "id",
                "department",
                "department__name",
                "report_date",
                "author",
                "author__first_name",
                "country",
                "country__korean",
            ]
            + models.PersonnelReport.TOTAL_LIST
            + ["description"]
        )


@admin.register(models.PersonnelReport)
class PersonnelReportAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = PersonnelReportResource
    fieldsets = (
        ("Basic Info", {"fields": ("department", "report_date", "country",)},),
        ("List Info", {"fields": models.PersonnelReport.TOTAL_LIST},),
        ("etc", {"fields": ("description",)},),
    )

    list_display = (
        "department",
        "report_date",
        "country",
        "get_office_subtotal",
        "get_field_subtotal",
        "get_total",
    )

    list_filter = (
        "department",
        "report_date",
        "country",
    )


# Register your models here.
