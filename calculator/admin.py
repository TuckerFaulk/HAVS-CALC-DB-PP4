from django.contrib import admin
from .models import Categories, Equipment, Calculator


"""Registers the categories model on the django admin site"""
admin.site.register(Categories)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    """Registers the equipment model on the django admin site"""

    list_display = ('category', 'make_and_model', 'slug', 'created_on')
    prepopulated_fields = {'slug': ('make_and_model',)}
    list_filter = ('created_on',)


@admin.register(Calculator)
class CalculatorAdmin(admin.ModelAdmin):
    """Registers the calculator model on the django admin site"""

    list_display = ('make_and_model', 'slug', 'author', 'exposure_duration_hours', 'exposure_duration_minutes')
    prepopulated_fields = {'slug': ('author', 'make_and_model', 'exposure_duration_hours', 'exposure_duration_minutes')}
