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
    email = models.EmailField()
    phone = models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_time_created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer,related_name="customer",on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150,blank=False,null=False)
    comapny_address = models.CharField(max_length=150,blank=False,null=False)
    company_city = models.CharField(max_length=150,blank=False,null=False)
    company_location = models.CharField(max_length=150,blank=False,null=False)
    company_pin = models.CharField(max_length=150,blank=False,null=False)
    company_district = models.CharField(max_length=150,blank=False,null=False)
    company_state = models.CharField(max_length=150,blank=False,null=False)
    company_gstin = models.CharField(max_length=150,blank=False,null=False)
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=150,blank=False,null=False)
    company_logo = models.TextField()
    product_list = models.ManyToManyField(Inventory,related_name="product")
    due_amount  = models.FloatField()
    sgst = models.FloatField()
    cgst = models.FloatField()
    status = models.BooleanField()
    invoice_type = models.CharField(max_length=150,blank=False,null=False)
    digital_signature = models.CharField(max_length=150,blank=False,null=False)

    def __str__(self):
        return str(self.id)
