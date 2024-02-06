from .models import Product, Color, Size, Material, Category

import csv
import os


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

def handle_upload_avatar(image):
    new_image_path = os.path.join('images', image.name)
    full_path = os.path.join('media', new_image_path)

    with open(full_path, 'wb+') as f:
        for chunk in image.chunks():
            f.write(chunk)

    return new_image_path