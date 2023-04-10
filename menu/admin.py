from django.contrib import admin

from . import models


EMPTY_VALUE_DISPLAY = '-empty-'


@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'slug',]
    empty_value_display = EMPTY_VALUE_DISPLAY


@admin.register(models.Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'menu', 'name', 'parent', 'slug', 'get_relatives']
    empty_value_display = EMPTY_VALUE_DISPLAY

    def get_relatives(self, obj):
        return [str(relatives) for relatives in obj.relatives.all()]


# delete in final cut
@admin.register(models.Relations)
class NodeRelations(admin.ModelAdmin):
    list_display = ['pk', 'ancestor', 'descendant']
    empty_value_display = EMPTY_VALUE_DISPLAY
