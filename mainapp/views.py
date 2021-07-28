from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def index(request):
    title = 'каталог'

    links_menu = [
        {'href': 'index', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'класика'}
    ]

    # for el in ProductCategory.objects.all():
    #     links_menu.append({'href': el.slug, 'name': el.name})



    products = Product.objects.all()[:4]

    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': products,

    }
    return render(request, 'mainapp/products.html', context)