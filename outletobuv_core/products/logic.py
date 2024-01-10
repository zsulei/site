from .models import Product, Color, Size, Material


def get_or_create_product(name=None,description=None,
                          category=None, price=None,
                          country=None,season=None,
                          article=None
                          ):
    product = Product.objects.get_or_create(
        article=article,
        defaults={
                'name': name,
                'category': category,
                'description': description,
                'country': country,
                'season': season,
                'price': price,
        }
    )
    