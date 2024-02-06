from django.urls import reverse_lazy
from .forms import ProductImageForm
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Size, Material, Color, Category
from django.core.paginator import Paginator
from .utils import test, handle_upload_avatar
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView


class IndexView(TemplateView):
    template_name = 'products/index.html'
    title = 'Outlet Obuv'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Store'


class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 15
    title = 'Outlet Obuv'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('pk')
        return queryset.filter(category_id=category_id) if category_id else queryset
    
    def get_context_data(self, *, object_list=None, **krwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs.get('category_id')
        product_color = self.object.colors
        product_material = self.object.materials

        sizes_query = Size.objects.filter(
                                          material=product_material,
                                          color=product_color
                                          )
        try:
            unique_sizes = {size.value for size in sizes_query}
            sorted_unique_sizes = sorted(unique_sizes, key=int)
        except:
            sorted_unique_sizes = sizes_query

        context['material'] = product_material
        context['color'] = product_color
        context['sizes'] = sorted_unique_sizes

        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductImageForm
    template_name = 'product/update_product.html'
    success_url = reverse_lazy('update_product_image')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.image = self.request.FILES['image']
        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('products:detail', kwargs={'pk': self.object.pk})


def product(request, product_id):

    product = Product.objects.get(id=product_id)

    product_color = product.colors
    product_material = product.materials

    size_queryset = Size.objects.filter(
        color=product_color,
        material=product_material
    )
    try:
        unique_sizes = {size.value for size in size_queryset}
        sorted_unique_sizes = sorted(unique_sizes, key=int)
    except:
        sorted_unique_sizes = size_queryset

    context = {
        'product': product,
        'color': product_color,
        'sizes': sorted_unique_sizes
    }
    return render(request, 'products/product.html', context)


def update_product_image(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        product.image = request.FILES.get('image')
        product.save()
        return redirect('product_detail', product_id=product.id)

    return redirect('product_detail', product_id=product.id)


def parse_tsgoods_view(request):

    file_path = 'C:/Users/2021/Desktop/site/TSGoods.trs'

    try:
        test(file_path)
        return HttpResponse("File parsed successfully.")
    except Exception as e:
        print(e)
        return HttpResponse(f"Error occurred: {e}")


def index(request):
    context = {
        'products': Product.objects.all(),
        'title': 'Store',
        'is_promotion': 'True',
    }
    return render(request, 'products/index.html', context)


def search_by_name(request):
    query_data = request.GET.get('search_holder')
    query_article = Product.objects.filter(article__icontains=query_data)
    query_name = Product.objects.filter(name__icontains=query_data)
    query_size = Product.objects.filter(size__value__icontains=query_data)
    queryset = query_article | query_name | query_size
    categories = Category.objects.all()

    context = {
        'products': queryset,
        'categories': categories
    }
    
    return render(request, 'products/search.html', context)


def about(request):
    return render(request, 'about.html')


def products(request, category_id=None, page_number=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    
    per_page = 15
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)
    categories = Category.objects.all()
    context = {
        'title': 'Outlet Obuv',
        'categories': categories,
        'products': products_paginator,
    }
    return render(request, 'products/products.html', context)
