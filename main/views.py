from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    product_list = Product.objects.all()
    context = {
        'npm' : '2406432513',
        'name': 'Vidya Pramudita Andini',
        'class': 'PBP D',
        'product' : 'Jersey',
        'price' : 650000,
        'category' : 'Clothes',
        'description' : 'A very comfortable jersey for you!',
        'product_list' : product_list
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_news.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "news_detail.html", context)

def show_xml(request):
    news_list = Product.objects.all()

def show_xml(request):
     news_list = Product.objects.all()
     xml_data = serializers.serialize("xml", news_list)
     return HttpResponse(xml_data, content_type="application/xml")