from django.urls import path

from . import views

app_name = 'menus'

urlpatterns = [
    path('one_menu/', views.one_menu, name='one_menu'),
    path('several_menus/', views.several_menus,
         name='several_menus'),
]
