from django.contrib import admin

from .models import *


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'city',
        'state',
    ]
    search_fields = [
        'name',
    ]
    list_filter = [
        'city',
        'state',
    ]


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
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
class CountryAdmin(admin.ModelAdmin):
    pass
