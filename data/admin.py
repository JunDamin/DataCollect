from django.contrib import admin
from import_export import resources
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


class DepartmentResource(resources.ModelResource):
    class Meta:
        model = models.Department
        fields = (
            "id",
            "name",
            "koica_code",
            "location",
            "location__korean",
            "is_active",
        )
        export = (
            "id",
            "name",
            "koica_code",
            "location",
            "location__korean",
            "is_active",
        )


@admin.register(models.Department)
class DepartmentAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = DepartmentResource
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
