from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError
import datetime 
import uuid


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id','date_time_created','date_created', 'name', 'hsn','base_price','sales_price','stock','store_id','unit')
        

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','date_time_created','date_created', 'name', 'logo','address','city','location','pincode','state','country','district','gst_number','gst_type','email','phone','store_id')
        
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
    
        read_only_fields = ('pdf',)
        

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
        fields = ( 'unique_id','phone','email','password')
        # extra_kwargs = {'password': {'write_only': True}}


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    numberofdate = serializers.IntegerField()
    confirmpassword = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ('numberofdate', 'phone','first_name','last_name', 'email','subscription_plan','password','confirmpassword')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        today = datetime.date.today()
        numertime = validated_data['numberofdate']
        enddate =  today + datetime.timedelta(days=numertime)
       
    
        user = CustomUser.objects.create(unique_id=str(uuid.uuid4())[:8],username=validated_data['phone'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],phone=validated_data['phone'],email=validated_data['email'],subscription_plan=validated_data['subscription_plan'],subscription_end=enddate)
        user.set_password(validated_data['password'])
        user.save()

        return user
       

    def validate_password(self,data):
        data = self.get_initial()
        password = data.get("password")
        password2 = data.get("confirmpassword")
        if password != password2:
            raise ValidationError("Password Not Match")
        return password

    def validate_user(self,data):
        data = self.get_initial()
        phone = data.get("phone")
        
        user = CustomUser.objects.get(phone=phone)
        if user is not None:
            raise ValidationError("User Already Exist")
        else:
            return phone
     
                

class UserAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}