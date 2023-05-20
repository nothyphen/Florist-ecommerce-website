from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import reverse
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    birth = models.DateField()
    image = models.ImageField(upload_to='images/') 

    class Meta:
        verbose_name_plural = "خریدار"
        verbose_name = "خریدار"

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=200)
    #image = models.ImageField(upload_to="images/")
     #image = ImageField()
     
    class Meta:
        verbose_name_plural = "گروه محصولات"
        verbose_name = "گروه محصولات"
    
    def __str__(self):
        return self.name

class Product(models.Model):
    STATUS = (
    ('y', 'Yes'),
    ('n', 'No'),
    )
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    info = models.TextField(default='')
    quantety = models.IntegerField()
    collaction = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=80, unique=True)
    trend = models.CharField(max_length=1, choices=STATUS)

    class Meta:
        verbose_name_plural = "محصولات"
        verbose_name = "محصولات"

    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS = (
    ('pr', 'Proccessing'),
    ('co', 'Completed'),
    ('ca', 'Cancelled'),
    ('on', 'ON Hold'),
    ('pe', 'Pending'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=STATUS)
    transation_id = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(default=2, null=True, blank=True)

    class Meta:
        verbose_name_plural = "سفارشات"
        verbose_name = "سفارشات"

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        
        return shipping
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "میزان سفارش"
        verbose_name = "میزان سفارش"

    def __str__(self):
        return str(self.product)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
 
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    street = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "ادرس"
        verbose_name = "ادرس"

    def __str__(self):
        return self.address

class Banner(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = "بنر"
        verbose_name = "بنر"

    def __str__(self):
        return self.name
    
class Subscribe(models.Model):
    email = models.EmailField()

class AboutUs(models.Model):
    twitter = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    detail = models.CharField(max_length=200)

class Contact(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

class CompanyMember(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)

class Faq(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()