from django.contrib import admin
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
    fieldsets = (("Basic Info", {"fields": ("personnel", "number", "report",)},),)

    list_display = (
        "personnel",
        "number",
        "report",
    )

    list_filter = (
        "personnel",
        "number",
        "report",
    )


class PersonnelInfoInline(admin.TabularInline):
    model = models.PersonnelInfo
    extra = 0


@admin.register(models.PersonnelReport)
class PersonnelReportAdmin(ImportExportMixin, admin.ModelAdmin):
    fieldsets = (
        ("Basic Info", {"fields": ("department", "report_date", "country",)},),
    )

    inlines = [PersonnelInfoInline]

    list_display = (
        "department",
        "report_date",
        "country",
    )

    list_filter = (
        "department",
        "report_date",
        "country",
    )


# Register your models here.
