from django.shortcuts import render
# from .models import Node, Menu, Relations


def one_menu(request):
    template = 'tests/one_menu.html'
    title = 'Проверка одного меню'
    context = {
        'title': title,
    }
    return render(request, template, context)


def several_menus(request, slug):
    template = 'tests/several_menu.html'
    title = 'Проверка нескольких меню'
    context = {
        'title': title,
    }
    return render(request, template, context)
