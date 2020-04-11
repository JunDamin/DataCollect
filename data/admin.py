from django.contrib import admin
from import_export.admin import ImportExportMixin
from . import models

# Register your models here.


@admin.register(models.Country, models.Region)
class ItemAdmin(ImportExportMixin, admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name",)


class DepartmentDetailInline(admin.TabularInline):
    model = models.DepartmentDetail
    extra = 0


@admin.register(models.Department)
class DepartmentAdmin(ImportExportMixin, admin.ModelAdmin):
    fieldsets = (("Basic Info", {"fields": ("name", "koica_code", "location",)},),)

    inlines = [DepartmentDetailInline]

    list_display = (
        "name",
        "koica_code",
        "location",
    )

    list_filter = (
        "name",
        "koica_code",
        "location",
    )
