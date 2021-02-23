from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError
from datetime import date


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
        depth = 2


class InvoiceWriteSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Invoice
        fields = "__all__"

class ComponySerializer(serializers.ModelSerializer):

    class Meta:
        model = Compony
        fields = "__all__"

class ExcelConvert(serializers.Serializer):
    files = serializers.FileField()


class TaxSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaxGroup
        fields = "__all__"


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('unique_id','first_name','last_name', 'phone', 'email','subscription_plan','subscription_start','subscription_end','subscription_status','user_status')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    numberofdate = serializers.IntegerField()
    class Meta:
        model = CustomUser
        fields = ('numberofdate','unique_id', 'phone','first_name','last_name', 'email','subscription_plan','subscription_start','subscription_end','subscription_status','user_status','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        today = date.today()
        
        user = CustomUser.objects.create(username=validated_data['phone'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],phone=validated_data['phone'],email=validated_data['email'],subscription_plan=validated_data['subscription_plan'])

        return user