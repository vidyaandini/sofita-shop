import datetime
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
from django.http import JsonResponse
import json

# Create your views here.
# Hapus filter di show_main karena sudah di-handle oleh AJAX
@login_required(login_url='/login')
def show_main(request):
    # filter_type = request.GET.get("filter", "all") # Dihapus
    # if filter_type == "all":
    product_list = Product.objects.all() # Cukup ambil semua, ini hanya untuk initial render
    # else:
    #     product_list = Product.objects.filter(user=request.user) # Dihapus
        
    context = {
        'npm' : '2406432513',
        'name': request.user.username ,
        'class': 'PBP D',
        # Biarkan product_list tetap ada untuk kompatibilitas, tapi AJAX yang akan mengambil data
        'product_list' : product_list, 
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_xml_by_id(request, product_id):
    try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json(request):
    # Ambil SEMUA produk tanpa filter user
    product_list = Product.objects.all().select_related('user')
    
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user else 'Anonymous',
        }
        for product in product_list
    ]
    
    return JsonResponse(data, safe=False)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = ProductForm(instance=product)  # ← ini bagian penting

    context = {
        'form': form
    }
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user
    price = request.POST.get("price")

    new_news = Product(
        name=name, 
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user,
        price=price
    )
    new_news.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def delete_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return JsonResponse({"message": "Produk berhasil dihapus!"}, status=200)
    except:
        return JsonResponse({"error": "Gagal menghapus produk"}, status=400)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url or image_url.strip() == '':
        # Return a default SVG placeholder for empty URLs
        svg_content = '''<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
            <rect width="400" height="300" fill="#f3f4f6"/>
            <text x="200" y="150" text-anchor="middle" fill="#9ca3af" font-family="Arial" font-size="16">No Image</text>
        </svg>'''
        return HttpResponse(svg_content, content_type='image/svg+xml')

    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()

        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        # On error, return the default SVG placeholder
        svg_content = '''<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
            <rect width="400" height="300" fill="#f3f4f6"/>
            <text x="200" y="150" text-anchor="middle" fill="#9ca3af" font-family="Arial" font-size="16">Image Error</text>
        </svg>'''
        return HttpResponse(svg_content, content_type='image/svg+xml')
    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        # Require authentication for Flutter app
        if not request.user.is_authenticated:
            return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)

        try:
            data = json.loads(request.body)
            name = strip_tags(data.get("name", "").strip())
            description = strip_tags(data.get("description", "").strip())
            category = data.get("category", "").strip()
            thumbnail = data.get("thumbnail", "").strip()

            # Handle price - ensure it's a valid decimal
            price_str = str(data.get("price", "0")).strip()
            try:
                price = float(price_str) if price_str else 0.0
            except (ValueError, TypeError):
                price = 0.0

            is_featured = bool(data.get("is_featured", False))

            # Validate required fields
            if not name:
                return JsonResponse({"status": "error", "message": "Name is required"}, status=400)

            if not description:
                return JsonResponse({"status": "error", "message": "Description is required"}, status=400)

            # Validate category choices - map Flutter categories to Django categories
            category_mapping = {
                'sepatu running': 'transfer',
                'jersey': 'update',
                'sepatu futsal': 'exclusive',
                'topi': 'match',
                'sepatu bola': 'rumor',
                'celana training': 'analysis'
            }
            category = category_mapping.get(category, 'update')

            user = request.user

            new_product = Product(
                name=name,
                description=description,
                category=category,
                thumbnail=thumbnail,
                price=price,
                is_featured=is_featured,
                user=user
            )
            new_product.save()

            # Return response expected by Flutter app
            response_data = {
                "status": "success",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                }
            }

            return JsonResponse(response_data, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON data"}, status=400)
        except Exception as e:
            print(f"Error creating product: {e}")
            return JsonResponse({"status": "error", "message": "Internal server error"}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)
    
def show_product_user(request):
    # Return empty list if not authenticated
    if not request.user.is_authenticated:
        return JsonResponse([], safe=False, status=200)
    
    qs = Product.objects.filter(user=request.user).select_related("user")
    
    data = [
        {
            "id": str(p.id),
            "name": p.name,
            "description": p.description,
            "price": p.price,
            "category": p.category,
            "thumbnail": p.thumbnail,
            "product_views": p.product_views,
            "created_at": p.created_at.isoformat() if p.created_at else None,
            "is_featured": p.is_featured,
            'user_id': p.user_id,
            "user_username": p.user.username,
        }
        for p in qs
    ]
    
    return JsonResponse(data, safe=False, status=200)