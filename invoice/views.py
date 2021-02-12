from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import filters
from  rest_framework.mixins import CreateModelMixin
# Create your views here.

class CreateInventory(CreateModelMixin,generics.GenericAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()

        return Response({
            "data": InventorySerializer(data, context=self.get_serializer_context()).data,
            "status": "success"
            })
    

class UpdateInventory(generics.UpdateAPIView):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    def get(self,request,*args,**kwargs):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.name = request.data.get("name")
        instance.hsn = request.data.get("hsn")
        instance.base_price = request.data.get("base_price")
        instance.sales_price = request.data.get("sales_price")
        instance.stock = request.data.get("stock")
        instance.store_id = request.data.get("store_id")
        instance.unit = request.data.get("unit")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()

        return Response({"data":serializer.data,"status":"success"})

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message":"deleted Successfully","status":"success"})
    

class SearchInventory(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def get(self,request,*args,**kwargs):
        queryset = Inventory.objects.all()
        name = request.GET.get('name','')
        instance = get_object_or_404(queryset,name=name)
        serializer = self.get_serializer(instance)
        

        return Response({"data":serializer.data,"status":"success"})

