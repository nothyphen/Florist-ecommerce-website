from django.urls import path
from . import views

app_name= 'web'

urlpatterns = [
    path('', views.index, name="index"),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('detail/<slug:slug>/', views.product_detail, name='detailproduct'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('orders/', views.orders, name="orders"),
    path('dashboard/', views.address, name="address"),
    path('profile-detail/', views.profile_detail, name="profile_detail"),
    path('category/<slug:slug>/', views.categoryList, name='category_list'),
    path('search/', views.SearchProduct, name='search'),
    #path('payment/', views.paymentinfo, name='payment_info'),
]
