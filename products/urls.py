from django.urls import path

from products.views import products, contacto, create_product_view, search_product_view, create_categoria_view, create_cliente_view, search_categoria_view

urlpatterns =[
    path('', products, name = 'products'),
    path('contacto/', contacto, name = 'contacto'),
    path('create-product/', create_product_view, name = 'create-product'),
    path('search-product/', search_product_view, name = 'search_product_view'),
    path('create-categoria/', create_categoria_view, name = 'create_categoria'),
    path('create-cliente/', create_cliente_view, name = 'create_cliente'),
    path('search-categoria/', search_categoria_view, name = 'search_categoria_view'),
    
]