from django.db import models
import uuid

from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    
    phone = models.CharField(max_length=150,null=True,blank=True)
    subscription_plan = models.CharField(max_length=100,null=True,blank=True)
    subscription_start = models.DateField(auto_now_add=True)
    subscription_end = models.DateField(null=True,blank=True)
    subscription_status = models.BooleanField(default=True)
    user_status = models.BooleanField(blank=False,null=False,default=True)
    unique_id = models.CharField(max_length=100,default=str(uuid.uuid4())[:8],primary_key=True)
    token = models.TextField()
    def __str__(self):
        return self.phone


class Inventory(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_time_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150,blank=False,null=False)
    hsn = models.CharField(max_length=150,blank=True,null=True)
    base_price = models.FloatField(blank=False,null=False)
    sales_price =  models.FloatField(blank=False,null=False)
    stock = models.IntegerField(blank=False,null=False)
    cgst = models.IntegerField()
    sgst = models.IntegerField()
    cess = models.IntegerField()
    others = models.IntegerField()
    unit = models.CharField(max_length=150,blank=False,null=False)

    def __str__(self):
        return self.name

class Customer(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_time_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150,blank=False,null=False)
    logo = models.TextField()
    address = models.CharField(max_length=150,blank=True,null=True)
    city = models.CharField(max_length=150,blank=True,null=True)
    location = models.CharField(max_length=150,blank=True,null=True)
    pincode = models.CharField(max_length=150,blank=True,null=True)
    state = models.CharField(max_length=150,blank=True,null=True)
    country = models.CharField(max_length=150,blank=True,null=True)
    district = models.CharField(max_length=150,blank=True,null=True)
    gst_number = models.CharField(max_length=150,blank=False,null=False)
    gst_type = models.CharField(max_length=150,blank=True,null=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=150,null=True,blank=True)
    store_id = models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return self.name
class OrderItems(models.Model):
    product = models.ForeignKey(Inventory,on_delete=models.CASCADE)
    qty = models.IntegerField()

    def __str__(self):
        return str(self.id)

    def total_of_items(self):
        total = 0
        total+=self.product.sales_price * self.qty
        return total

class Invoice(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_time_created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer,related_name="customer",on_delete=models.CASCADE,null=True,blank=True)
    company_name = models.CharField(max_length=150,blank=False,null=False)
    company_address = models.CharField(max_length=150,blank=False,null=False)
    company_city = models.CharField(max_length=150,blank=False,null=False)
    company_location = models.CharField(max_length=150,blank=False,null=False)
    company_pin = models.CharField(max_length=150,blank=False,null=False)
    company_district = models.CharField(max_length=150,blank=False,null=False)
    company_state = models.CharField(max_length=150,blank=False,null=False)
    company_gstin = models.CharField(max_length=150,blank=False,null=False)
    company_email = models.EmailField()
    company_gst_type = models.CharField(max_length=150,blank=True,null=True)
    company_phone = models.CharField(max_length=150,blank=False,null=False)
    company_logo = models.TextField()
    product_list = models.ManyToManyField(OrderItems,related_name="orderitems")
    due_amount  = models.FloatField()
    sgst = models.FloatField()
    cgst = models.FloatField()
    status = models.BooleanField()
    invoice_type = models.CharField(max_length=150,blank=False,null=False)
    company_signature = models.TextField()
    company_id = models.CharField(max_length=150,null=True,blank=True)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return str(self.id)


class Compony(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_time_created = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=150)
    company_address = models.CharField(max_length=150)
    company_city = models.CharField(max_length=150)
    company_location = models.CharField(max_length=150)
    company_pin = models.CharField(max_length=150)
    company_district = models.CharField(max_length=150)
    company_satate = models.CharField(max_length=150)
    company_gstin = models.CharField(max_length=150)
    company_email = models.CharField(max_length=150)
    company_phone = models.CharField(max_length=150)
    company_logo = models.TextField()
    company_signature = models.TextField()
    
    company_id = models.CharField(max_length=150,default=str(uuid.uuid4())[:8],primary_key=True)


class TaxGroup(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_time_created = models.DateTimeField(auto_now_add=True)
    hsn_code = models.CharField(max_length=150)
    hsn_sgst = models.CharField(max_length=150)
    hsn_cgst = models.CharField(max_length=150)
    hsn_cess = models.CharField(max_length=150)
    hsn_others = models.CharField(max_length=150)
    hsn_user_id = models.CharField(max_length=150,default=str(uuid.uuid4())[:8])

class Units(models.Model):
    name=models.CharField(max_length=100,default=str(uuid.uuid4())[:8])
    short_name=models.CharField(max_length=100,default=str(uuid.uuid4())[:8])
    status=models.BooleanField()
    