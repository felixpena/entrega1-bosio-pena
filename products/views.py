
from django.shortcuts import render
from django.http import HttpResponse

from products.models import Products, Categoria, Cliente
from products.forms import Product_form, Categoria_form, Cliente_form

# Create your views here.
def products(request):
    print(request.method)
    productos = Products.objects.all()
    context = {'productos':productos}
    return render(request, 'products.html', context=context)

def contacto(request):
    return render(request, 'contacto.html')

def create_product_view(request):
    if request.method == 'GET':
        form = Product_form()
        context = {'form':form}
        return render(request, 'create_product.html', context=context)
    else:
        form = Product_form(request.POST)
        if form.is_valid():
            new_product = Products.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                SKU = form.cleaned_data['SKU'],
                active = form.cleaned_data['active'],
            )
            context ={'new_product':new_product}
        return render(request, 'create_product.html', context=context)

def search_product_view(request):
    print(request.GET)
    #product = Products.objects.get()
    products = Products.objects.filter(name__contains = request.GET['search'])
    context = {'products':products}
    return render(request, 'search_product.html', context = context)


def create_categoria_view(request):
    if request.method == 'GET':
        form = Categoria_form()
        context = {'form':form}
        return render(request, 'create_categoria.html', context=context)
    else:
        form = Categoria_form(request.POST)
        if form.is_valid():
            new_categoria = Categoria.objects.create(
                name = form.cleaned_data['name'],

                description = form.cleaned_data['description'],

            )
            context ={'new_categoria':new_categoria}
        return render(request, 'create_categoria.html', context=context)


def create_cliente_view(request):
    if request.method == 'GET':
        form = Cliente_form()
        context = {'form':form}
        return render(request, 'create_cliente.html', context=context)
    else:
        form = Cliente_form(request.POST)
        if form.is_valid():
            new_cliente = Cliente.objects.create(
                nombre = form.cleaned_data['nombre'],

                dni = form.cleaned_data['dni'],
                
            )
            context ={'new_cliente':new_cliente}
        return render(request, 'create_cliente.html', context=context)


# desarrollo buscador Categoria y Cliente:


def search_categoria_view(request):
    print(request.GET)
    #categoria = Categoria.objects.get()
    categoria = Categoria.objects.filter(name__contains = request.GET['search'])
    context = {'categoria':categoria}
    return render(request, 'search_categoria.html', context = context)


