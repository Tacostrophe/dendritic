from django.shortcuts import render
# from .models import Node, Menu, Relations


def one_menu(request):
    template = 'tests/one_menu.html'
    # group = get_object_or_404(Group, slug=slug)
    # posts = group.posts.all()
    # paginator = Paginator(posts, POSTS_PER_PAGE)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    title = 'Проверка одного меню'
    context = {
        'title': title,
        # 'slug': slug,
    }
    return render(request, template, context)


def several_menus(request, slug):
    template = 'tests/several_menu.html'
    title = 'Проверка нескольких меню'
    context = {
        'title': title,
        # 'slug': slug,
    }
    return render(request, template, context)
