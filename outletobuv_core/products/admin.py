from django.contrib import admin
from . import models


admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.Material)
admin.site.register(models.Color)
admin.site.register(models.Size)
