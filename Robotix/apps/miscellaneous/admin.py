from django.contrib import admin

from import_export.admin import ExportMixin

from .models import *


@admin.register(College)
class CollegeAdmin(ExportMixin, admin.ModelAdmin):
    list_display = [
        'name',
        'abbv',
        'city',
    ]
    search_fields = [
        'name',
        'abbv',
    ]
    list_filter = [
        'city',
        'state',
    ]


@admin.register(State)
class StateAdmin(ExportMixin, admin.ModelAdmin):
    list_filter = [
        'country__name',
    ]
    list_display = [
        'name',
        'country',
    ]
    search_fields = [
        'name',
        'country__name',
    ]


@admin.register(Country)
class CountryAdmin(ExportMixin, admin.ModelAdmin):
    pass
