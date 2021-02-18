from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError



class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id','date_time_created','date_created', 'name', 'hsn','base_price','sales_price','stock','store_id','unit')
        

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','date_time_created','date_created', 'name', 'logo','address','city','location','pincode','state','country','district','gst_number','gst_type','email','phone')
        
        extra_kwargs = {"address": {"error_messages": {"required": "Give yourself a username"}}}

    def validate_name(self,data):
        data = self.get_initial()
        name = data.get("name")
        if len(name) < 4:
            raise ValidationError("Minimum 4 Character")
        return name
    
    def validate_gst(self,data):
        
        gst = self.data.get("gst_number")
        if len(gst) == 0:
            raise ValidationError("Gst Number Not Valid")

class InvoiceReadSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Invoice
        fields = "__all__"
        depth = 1


class InvoiceWriteSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Invoice
        fields = "__all__"
        