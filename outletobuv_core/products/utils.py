from .models import Product, Color, Size, Material, Category

import csv


def test(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            try:
                article = row['Articul']
                name = row['GoodName'].split()[0]
                category = row['GoodTypeFull']
                material_name = row['Material']
                season = row['Season']
                color_name = row['Color']
                price = row['RetailPrice']
                size_value = row['TheSize']

                this_color, _ = Color.objects.get_or_create(name=color_name)
                this_material, _ = Material.objects.get_or_create(name=material_name)


                # print(f'Артикул {articul} Категория {category} Сезон {season} Материал {material} Цвет {color} Размер {size} Цена {price}')
                category, created = Category.objects.get_or_create(title=category)
                product, created = Product.objects.get_or_create(
                    article=article,
                    name=name,
                    category=category,
                    season=season,
                    price=price,
                    materials=this_material,
                    colors=this_color
                )


                existed_size = Size.objects.filter(
                    product=product,
                    value=size_value
                )
                if not existed_size.exists():
                    this_size = Size.objects.create(
                        product=product,
                        value=size_value
                    )
                    this_size.color.add(this_color)
                    this_size.material.add(this_material)
                    this_size.save()
            except Exception as e:
                print(f'Произошла ошибка:  {e}')



        # "Articul";"GoodTypeFull";"Category";
        # "WarehouseQuantity";"Material";"GoodName";
        # "PCName";"TheSize";"Season";
        # "PriceDiscountPercent";"Color";"RetailPrice"


# def products_from_csv(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         reader = file.readlines()
#         for row in reader:
#             splitted_line = row.split(';')
#             article = splitted_line[0].replace('"', '')
#             country = splitted_line[6].replace('"', '')
#             season = splitted_line[8].replace('"', '')
#             price = splitted_line[-1]
#             material_name = splitted_line[4].replace('"', '')
#             try:
#                 color_name = splitted_line[5].split(',')[0].split(' ')[1]
#             except IndexError as e:
#                 color_name = ''
#             size_value = splitted_line[5].split()[-1].replace('"', '')

#             print(article, country, season, price, material_name, color_name, size_value)

#             material, _ = Material.objects.get_or_create(name=material_name)
#             color, _ = Color.objects.get_or_create(name=color_name)
            
#             create_product(article, country, 
#                    season, price, 
#                    material, color, 
#                    size_value)


# def create_product(article, country, 
#                    season, price, 
#                    material, color, 
#                    size_value):
#     product = Product(
#         article=article,
#         country = country,
#         season=season,
#         price=price,
#     )
#     product.materials.set(material)
#     product.colors.set(color)
#     product.save()

#     size = Size.objects.get_or_create(value=size_value)
#     size.item.add(article)
#     size.material.add(material)
#     size.color.add(color)
#     size.save()



# def parse_tsgoods(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         lines = file.readlines()

#         for index, row in enumerate(lines):
#             if index == 0:
#                 continue
#             else:
#                 # Extracting data from each row
#                 splitted_line = row.split(';')
#                 article = splitted_line[0].replace('"', '')
#                 country = splitted_line[6].replace('"', '')
#                 season = splitted_line[8].replace('"', '')
#                 price = splitted_line[-1]
#                 material_name = splitted_line[4].replace('"', '')
#                 try:
#                     color_name = splitted_line[5].split(',')[0].split(' ')[1]
#                 except IndexError as e:
#                     color_name = ''
#                 size_value = splitted_line[5].split()[-1].replace('"', '')

                
#                 # Get or create Material and Color instances
#                 material, _ = Material.objects.get_or_create(name=material_name)
#                 color, _ = Color.objects.get_or_create(name=color_name)

#                 # Check if a Product with the same article already exists
#                 product, created = Product.objects.get_or_create(article=article)

#                 # Add new materials or colors if they are not already associated with the product
#                 if not product.materials.filter(name=material_name).exists():
#                     product.materials.add(material)
#                 if not product.colors.filter(name=color_name).exists():
#                     product.colors.add(color)

#                 # Handle sizes
#                 handle_sizes(product, size_value)



# def handle_sizes(product, size_value):
#     size, _ = Size.objects.get_or_create(value=size_value)
#     product.sizes.add(size)
