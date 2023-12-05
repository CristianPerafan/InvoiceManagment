from django.db import models

# Create your models here.

class Customer(models.Model):
    clietn_id = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    born_date = models.DateField()
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.CharField(max_length=100)

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100,primary_key=True)
    client_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date = models.DateField()

class Product(models.Model):
    product_id = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()

class Detail(models.Model):
    invoice_number = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    detail_number = models.CharField(max_length=100,primary_key=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)


