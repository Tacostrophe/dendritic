from django import template
from django.db.models import Q
from menu import models


register = template.Library()


@register.inclusion_tag('core/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context.get('request')
    if (request):
        slug = request.GET.get('node')
    slug = (slug or '')
    menu = {}
    nodes = models.Node.objects.filter(
        Q(parent__isnull=True) |
        Q(parent__descendants__descendant__slug=slug) |
        Q(parent__children__slug=slug) |
        Q(parent__slug=slug),
        menu__name=menu_name
    ).distinct()
    print(f'{str(nodes.query)=}')
    menu['nodes'] = nodes
    return menu
