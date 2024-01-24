from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from products.models import Product, Size, Material, Color, Category
from django.core.paginator import Paginator
from .utils import test


def product(request, product_id):
    
    product = Product.objects.get(id=product_id)

    product_color = product.colors
    product_material = product.materials

    size_queryset = Size.objects.filter(
        color=product_color,
        material=product_material
    )
    try:
        unique_sizes = {size.value for size in size_queryset}
        sorted_unique_sizes = sorted(unique_sizes, key=int)
    except:
        sorted_unique_sizes = size_queryset

    context = {
        'product': product,
        'color': product_color,
        'sizes': sorted_unique_sizes
    }

    return render(request, 'products/product.html', context)


def parse_tsgoods_view(request):
    file_path = 'C:/Users/2021/Desktop/site/TSGoods.trs'
    # test(file_path)
    # return HttpResponse(redirect('products:index'))

    try:
        test(file_path)
        return HttpResponse("File parsed successfully.")
    except Exception as e:
        print(e)
        return HttpResponse(f"Error occurred: {e}")


def index(request):
    context = {
        'products': Product.objects.all(),
        'title': 'Store',
        'is_promotion': 'True',
    }
    return render(request, 'products/index.html', context)


def about(request):
    return render(request, 'about.html')



def products(request, category_id=None, page_number=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    
    per_page = 15
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)
    categories = Category.objects.all()
    context = {
        'title': 'Store- Каталог',
        'categories': categories,
        'products': products_paginator,
    }
    return render(request, 'products/products.html', context)
