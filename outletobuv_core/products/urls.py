from django.urls import path
from . import views
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.conf.urls.static import static

from .views import products, index, product, parse_and_insert

app_name = 'products'

urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    path('', index, name='index'),
    path('<int:product_id>/', product, name='detail'),
    path('parse/', parse_and_insert, name='parse'),
    path('category/<int:category_id>/', products, name='category'),
    path('page/<int:page_number>/', products, name='paginator'),
    # path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    # path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)