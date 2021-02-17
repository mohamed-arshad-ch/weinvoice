from django.db import models

# Create your models here.

class Inventory(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_time_created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=150,blank=False,null=False)
    hsn = models.CharField(max_length=150,blank=True,null=True)
    base_price = models.FloatField(blank=False,null=False)
    sales_price =  models.FloatField(blank=False,null=False)
    stock = models.IntegerField(blank=False,null=False)
    store_id = models.CharField(max_length=150,blank=False,null=False)
    unit = models.CharField(max_length=150,blank=False,null=False)

    def __str__(self):
        return self.name

class Customer(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_time_created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=150,blank=False,null=False)
    logo = models.CharField(max_length=1000,blank=True,null=True)
    address = models.CharField(max_length=150,blank=True,null=True)
    city = models.CharField(max_length=150,blank=True,null=True)
    location = models.CharField(max_length=150,blank=True,null=True)
    pincode = models.CharField(max_length=150,blank=True,null=True)
    state = models.CharField(max_length=150,blank=True,null=True)
    country = models.CharField(max_length=150,blank=True,null=True)
    district = models.CharField(max_length=150,blank=True,null=True)
    gst_number = models.CharField(max_length=150,blank=False,null=False)
    gst_type = models.CharField(max_length=150,blank=True,null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return self.name
