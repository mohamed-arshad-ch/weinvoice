from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
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
        

        serializer = InventorySerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
        

        return Response({"data":serializer.data,"status":"success"})

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"status":"success","message":"deleted Successfully","status":"success"})
    

# class SearchInventory(generics.ListAPIView):
#     queryset = Inventory.objects.all()
#     serializer_class = InventorySerializer

#     def get(self,request,*args,**kwargs):
#         queryset = Inventory.objects.all()
#         name = request.GET.get('name','')
#         instance = get_object_or_404(queryset,name=name)
#         serializer = self.get_serializer(instance)
        

#         return Response({"data":serializer.data,"status":"success"})




class SortInventory(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['date_created','name','hsn','base_price','sales_price','stock','store_id','unit']
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'
    
    # filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    # print(filter_backends)
    # search_fields = ['store_id','name','hsn','base_price','sales_price','stock','store_id','unit']
    ordering_fields = ['date_created','name','hsn','base_price','sales_price','stock','store_id','unit']

class PartialSearch(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    print(filter_backends)
    search_fields = ['name']
    
    
        

    