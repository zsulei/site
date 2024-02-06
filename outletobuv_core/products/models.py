from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='Категория'
        verbose_name_plural = 'Категории'


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Material(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Size(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)    
    color = models.ManyToManyField(Color)
    material = models.ManyToManyField(Material)
    value = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        color = ' '.join(str(color) for color in self.color.all())
        material = ' '.join(str(material) for material in self.material.all())
        return f'{self.value} | {self.product} | {color} | {material}'
    
    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Product(models.Model):
    article = models.CharField(max_length=22)
    name = models.CharField(max_length=100)
    materials = models.ForeignKey(Material, on_delete=models.CASCADE)
    colors = models.ForeignKey(Color, on_delete=models.CASCADE)
    is_popular = models.BooleanField(default=False)
    season = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    image = models.ImageField(upload_to='imgs/products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country = models.CharField(max_length=200)
    description = models.CharField(max_length=250, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'
        ordering = ['article']

    def __str__(self) -> str:
        return f'{self.article}'
    