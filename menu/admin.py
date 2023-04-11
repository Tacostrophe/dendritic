from django.contrib import admin

from . import models


EMPTY_VALUE_DISPLAY = '-empty-'


@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name']
    empty_value_display = EMPTY_VALUE_DISPLAY
    ordering = ['name']


@admin.register(models.Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ['menu', 'name', 'parent']
    empty_value_display = EMPTY_VALUE_DISPLAY
    ordering = ['menu__name', 'parent', 'pk']
