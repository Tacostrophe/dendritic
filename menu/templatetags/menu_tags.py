from django import template
from django.db.models import Q
from menu import models


register = template.Library()


@register.inclusion_tag('core/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context.get('request')
    if (request):
        node_id = request.GET.get('node_id')
    node_id = (node_id or 0)
    menu = {}
    nodes = models.Node.objects.filter(
        Q(parent__isnull=True) |
        Q(parent__descendants__descendant__id=node_id) |
        Q(parent__children__id=node_id) |
        Q(parent__id=node_id),
        menu__name=menu_name
    ).distinct()
    print(nodes)
    children = {}
    result_node_list = []
    nodes_index = len(nodes) - 1
    while (nodes_index >= 0):
        node = nodes[nodes_index]
        if (node.id in children):
            node.subnodes = children[node.id][::-1]
        else:
            node.subnodes = []
        if (node.parent):
            if (node.parent.id in children):
                children[node.parent.id].append(node)
            else:
                children[node.parent.id] = [node]
        else:
            result_node_list.append(node)
        nodes_index -= 1
    menu['nodes'] = result_node_list[::-1]
    return menu
