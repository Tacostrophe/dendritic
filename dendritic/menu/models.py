from django.db import models


class Menu(models.Model):
    name = models.CharField('menu_name', max_length=64)
    url = models.URLField('url_to_menu_item', max_length=64)
