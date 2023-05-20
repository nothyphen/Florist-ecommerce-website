from django.contrib import admin
from .models import Category, Customer, Contact, CompanyMember, AboutUs, ShippingAddress, Product, Order, OrderItem,Banner, Subscribe, Faq
# Register your models here.
class CategotyList(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Category, CategotyList)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Banner)
admin.site.register(Subscribe)
admin.site.register(AboutUs)
admin.site.register(Contact)
admin.site.register(CompanyMember)
admin.site.register(Faq)