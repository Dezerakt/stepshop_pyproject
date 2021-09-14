from django.shortcuts import render

from mainapp.models import Product


def products(request):
    title = 'продукты | каталог'

    links_menu = [
        {'href': 'products_all', 'name': 'Все'},
        {'href': 'products_shoegaze', 'name': 'Shoegaze'},
        {'href': 'products_rock', 'name': 'Rock'},
        {'href': 'products_metal', 'name': 'Metal'},
        {'href': 'products_postpunk', 'name': 'Post-Punk'},
    ]

    products_all = Product.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_all,
    }

    return render(request, 'mainapp/products.html', context)


def product(request):
    return render(request, 'mainapp/product.html')