from django.contrib import admin

from . import models


EMPTY_VALUE_DISPLAY = '-empty-'


@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'slug',]
    empty_value_display = EMPTY_VALUE_DISPLAY


@admin.register(models.Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'menu', 'name', 'parent', 'slug',]
    empty_value_display = EMPTY_VALUE_DISPLAY
