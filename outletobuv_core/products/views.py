from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from products.models import Product, Size, Material, Color
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction


# def parse_db(request):
#     file = 'C:/Users/2021/Desktop/site/TSGoods.trs'
#     f = open(file, 'r', encoding='utf-8')
#     lines = f.readlines()

#     for line in lines:
#         splitted_line = line.split(';')
#         article = splitted_line[0].replace('"', '')
#         country = splitted_line[6].replace('"', '')
#         season = splitted_line[8].replace('"', '')
#         price = splitted_line[-1]

#         category_title = splitted_line[1].replace('"', '')
#         category, created = Category.objects.get_or_create(title=category_title)

#         material_title = splitted_line[4].replace('"', '')
#         material, created = Material.objects.get_or_create(title=material_title)

#         try:
#             color = splitted_line[5].split(',')[0].split(' ')[1]
#         except IndexError as e:
#             color = ''

#         # color_title = splitted_line[4].replace('"', '')
#         color, created = Color.objects.get_or_create(title=color)

#         size = splitted_line[5].split()[-1].replace('"', '')
#         size, created = Size.objects.get_or_create(title=size)

#         if article == '\ufeffArticul':
#             continue
#         else:
#             exist_product = Product.objects.filter(article=article).first()

#             if exist_product:

#                 if exist_product.material == material_title:

#                     if exist_product.color == color:

#                         exist_product.size.add(size)
#                         exist_product.save()
                
#                     exist_product.color.set(color)
#                     # exist_product.color = color
#                     # exist_product.country = country
#                     exist_product.size.add(size)
#                     exist_product.save()
                
#                 exist_product.color.add(color)                
#                 exist_product.material.add(material_title)
#                 # exist_product.country = country
#                 # exist_product.season = season
#                 # exist_product.price = price
#                 # exist_product.category = category
#                 exist_product.size.add(size)
#                 exist_product.save()
                
#             else:
#                 product = Product(
#                     article=article,
#                     country=country,
#                     season=season,
#                     price=price,
#                     category=category,
#                 )
#                 product.save()
#                 product.size.add(size)
#                 product.material.set(Material.objects.get_or_create(name=material_title)[0])
#                 product.color.set(Color.objects.get_or_create(name=color)[0])

#     return redirect(index)


# def parse_and_insert(request):
#     file = 'C:/Users/2021/Desktop/site/TSGoods.trs'
#     f = open(file, 'r', encoding='utf-8')
#     lines = f.readlines()

#     for row in lines:

#         splitted_line = row.split(';')
#         article = splitted_line[0].replace('"', '')
#         country = splitted_line[6].replace('"', '')
#         season = splitted_line[8].replace('"', '')
#         price = splitted_line[-1]
#         category = splitted_line[1].replace('"', '')
#         name = 'Поменяйте название'
#         description = 'Поменяйте описание'

#         try:
#             color = splitted_line[5].split(',')[0].split(' ')[1]
#         except IndexError as e:
#             color = ''
#         # color, created = Color.objects.get_or_create(name=color)


#         material = splitted_line[4].replace('"', '')
#         # material, created = Material.objects.get_or_create(name=material_title)

#         size = splitted_line[5].split()[-1].replace('"', '')
#         # size, created = Size.objects.get_or_create(value=size)
        
#         existed_product = Product.objects.filter(article=article).first()

#         if existed_product:
#             #Если такой артикул есть:
#             if existed_product.materials.filter(name=material).first():
#                 #Если есть такой материал:
#                 if existed_product.colors.filter(name=color).first():
#                     #Если есть такой цвет:
#                     size_obj, created_size = Size.objects.get_or_create(value=size)
#                     existed_product.sizes.add(size_obj)
#                     #Привязываем размер к продукту с таким артикулом, материлом и цветом
#                 else:
#                     #Если нет такого цвета,
#                     # мы создаем новый продукт
#                     # с таким артикулом и новым цветом
#                     product, created = Product.objects.get_or_create(
#                         article=article,
#                         defaults={
#                             'name': name,
#                             'category': category,
#                             'description': description,
#                             'country': country,
#                             'season': season,
#                             'price': price,
#                         }
#                     )
#                     size_obj, created_size = Size.objects.get_or_create(value=size)
#                     product.sizes.add(size_obj)
#                     color_obj, created_material = Color.objects.get_or_create(name=color)
#                     product.colors.add(color_obj)
#             else:
#                 #Если нет такого матерала,
#                 # мы создаем новый продукт
#                 # с таким артикулом и новым материалом
#                 material_obj, created_material = Material.objects.get_or_create(name=material)

#                 product, created = Product.objects.create(
#                     article=article,
#                     defaults={
#                         'name': name,
#                         'category': category,
#                         'description': description,
#                         'country': country,
#                         'season': season,
#                         'price': price,
#                     }
#                 )
#                 product.materials.add(material_obj)
#         else:
#             #Есои нет такого артикула, 
#             #то создаем продукт с таким артикулом
#             product, created = Product.objects.create(
#                 article=article,
#                 defaults={
#                     'name': name,
#                     'category': category,
#                     'description': description,
#                     'country': country,
#                     'season': season,
#                     'price': price,
#                 }
#             )

#             material_obj, created_material = Material.objects.get_or_create(name=material)
#             product.materials.add(material_obj)

#             color_obj, created_material = Color.objects.get_or_create(name=color)
#             product.colors.add(color_obj)

#             size_obj, created_size = Size.objects.get_or_create(value=size)
#             product.sizes.add(size_obj)
#     else:
        
        
#         print(f"Product {product.article} created successfully.")
        
#     return render(request, 'products/index.html')


def index(request):
    context = {
        'products': Product.objects.all(),
        'title': 'Store',
        'is_promotion': 'True',
    }
    return render(request, 'products/index.html', context)


def product(request, product_id):
    context = {
        'product': get_object_or_404(Product, pk=product_id),
    }
    return render(request, 'products/product.html', context)



def products(request, category_id=None, page_number=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)
    # categories = Category.objects.all()
    context = {
        'title': 'Store- Каталог',
        # 'categories': categories,
        'products': products_paginator,
    }
    return render(request, 'products/products.html', context)
