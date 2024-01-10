from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name


class Size(models.Model):
    Product = models.ManyToManyField('Product')
    Color = models.ManyToManyField(Color)
    Material = models.ManyToManyField(Material)
    value = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.value


class Product(models.Model):
    article = models.CharField(max_length=22)
    name = models.CharField(max_length=100)
    is_popular = models.BooleanField(default=False)
    season = models.CharField(max_length=200)
    materials = models.ForeignKey(Material, on_delete=models.CASCADE)
    colors = models.ForeignKey(Color, on_delete=models.CASCADE)
    sizes = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8,decimal_places=0)
    image = models.ImageField(upload_to='imgs/products')
    category = models.CharField(max_length=250)
    country = models.CharField(max_length=200)
    description = models.CharField(max_length=250, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'

    def __str__(self) -> str:
        return f'{self.article}'
    