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
    value = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.value


class Product(models.Model):
    article = models.CharField(max_length=22)
    name = models.CharField(max_length=100)
    is_popular = models.BooleanField(default=False)
    season = models.CharField(max_length=200)
    materials = models.ManyToManyField(Material)
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size)
    price = models.CharField(max_length=5,default='noprice')
    image = models.ImageField(upload_to='imgs/products')
    category = models.CharField(max_length=250)
    country = models.CharField(max_length=200)
    description = models.CharField(max_length=250, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'

    def __str__(self) -> str:
        return f'{self.article}'
    

class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, models.CASCADE)


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    


class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
