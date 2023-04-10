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
    result_node_list = []
    nodes_index = len(nodes) - 1
    while (nodes_index >= 0):
        node = nodes[nodes_index]
        if (not hasattr(node, 'subnodes')):
            node.subnodes = []
        if (node.parent):
            parent_index = nodes.index(node.parent)
            if (not hasattr(nodes[parent_index], 'subnodes')):
                nodes[parent_index].subnodes = []
            nodes[parent_index].subnodes.append(node)
        else:
            result_node_list.append(node)
        nodes_index -= 1
    menu['nodes'] = result_node_list[::-1]
    return menu
