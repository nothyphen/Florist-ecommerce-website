from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.http import JsonResponse
import json
import logging
from django.urls import reverse
# Create your views here.
def index(request):
    product = Product.objects.filter(trend='y')
    category = Category.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items
        
    else:
        cartItem = ''
        items = []
        order = {
            'get_cart_total':0,
            'cartItems' : cartItem,
        }
    context = {
            'items' : items,
            'order' : order,
            'cartItems' : cartItem,
            'products' : product,
            'categories' : category,
        }
    return render(request, 'index.html', context=context)

def shop(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items
        
    else:
        items = []
        order = {
            'get_cart_total':0,
        }
        cartItem = ''

    product = Product.objects.all()
    context = {
        'items' : items,
        'order' : order,
        'cartItems' : cartItem,
        'products' : product,
        'cartItems' : cartItem,
    }
    return render(request, "shop.html", context=context)

def product_detail(request, slug):
    product = Product.objects.filter(slug=slug)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_total':0,
            'cartItems' : cartItem,
        }
    context = {
        'product' : product,
        'items' : items,
        'order' : order,
        'cartItems' : cartItem,
    }
    return render(request, 'product-single.html', context=context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items
    else :
        items = []
        order = {
            'get_cart_total':0,
            'shipping' : False
        }
        cartItem = ''
    context = {
            'items' : items,
            'order' : order,
            'cartItems' : cartItem,
        }
    return render(request, 'checkout.html', context=context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items
        
    else:
        items = []
        order = {
            'get_cart_total':0,
            'cartItems' : cartItem,
        }
    context = {
            'items' : items,
            'order' : order,
            'cartItems' : cartItem,
        }
    return render(request, 'cart.html', context=context)

def confirm(request):
    return render(request, 'confirmation.html')

def contact(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_total':0,
            'cartItems' : cartItem,
        }
    context = {
        'items' : items,
        'order' : order,
        'cartItems' : cartItem,
    }
    return render(request, "contact.html")

def about(request):
    about = AboutUs.objects.all()
    context = {
        'abouts' : about,
    }
    return render(request, 'about.html', context=context)

def error404(request):
    return render(request, '404.html')

def faq(request):
    faq = Faq.objects.all()
    context = {
        'faqs' : faq,
    }
    return render(request, 'faq.html', context=context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(action)
    print(productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == "removeAll":
        orderItem.quantity = 0

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('item was added', safe=False)

def processOrder(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        street = request.POST['street']
        zipcode = request.POST['zipcode']
        shipping, created = ShippingAddress.objects.get_or_create(customer=customer, order=order, address=address, city=city, state=state, street=street, zipcode=zipcode)
    return redirect('/payment/')

def dashboard(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items
        customer = Customer.objects.filter(user=request.user)
        allorders = Order.objects.filter(customer=request.user.customer, complete=True)
        
    else:
        items = []
        order = {
            'get_cart_total':0,
            'cartItems' : cartItem,
        }
    context = {
            'user' : customer,
            'items' : items,
            'order' : order,
            'cartItems' : cartItem,
            'allorders' : allorders,
        }
    return render(request, 'dashboard.html', context=context)

def orders(request):
    return render(request, 'order.html')

def address(request):
    return render(request, 'address.html')

def profile_detail(request):
    return render(request, 'profile-details.html')