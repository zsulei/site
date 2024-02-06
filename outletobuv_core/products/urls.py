from django.urls import path
from . import views
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.conf.urls.static import static

from .views import about, products, index, product, parse_tsgoods_view, search_by_name, update_product_image,\
    ProductsListView, ProductDetailView, ProductUpdateView


app_name = 'products'

urlpatterns = [
        
    # path('', index, name='index'),
    # path('category/<int:category_id>/', products, name='category'),
    # path('page/<int:page_number>/', products, name='paginator'),
    # path('detail/<int:product_id>/', product, name='detail'),

    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:pk>/', ProductsListView.as_view(), name='category'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('product/<int:pk>/update_image/', ProductUpdateView.as_view(), name='update_product_image'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    
    path('search/', search_by_name, name='search'),
    path('about/', about, name='about'),
    path('update_image/<int:product_id>/', update_product_image, name='update_image'),
    path('parse-tsgoods/', parse_tsgoods_view, name='parse_tsgoods'),

    # path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    # path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        