from rest_framework import serializers
from .models import *

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id','date_time_created','date_created', 'name', 'hsn','base_price','sales_price','stock','store_id','unit')