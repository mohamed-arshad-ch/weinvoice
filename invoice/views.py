from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
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
        else:
            errorr = serializer.errors
            errorr['status'] = "Error"

            return Response(errorr)
        

        

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"status":"success","message":"deleted Successfully","status":"success"})
    





class SortInventory(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['date_created','name','hsn','base_price','sales_price','stock','store_id','unit']
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'
    
    
    ordering_fields = ['date_created','name','hsn','base_price','sales_price','stock','store_id','unit']

class PartialSearch(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
   
    search_fields = ['name']




class CreateForCustomer(CreateModelMixin,generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"Fail": "blablal"})

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"Success": "msb blablabla"},  headers=headers)
        # serializer = self.get_serializer(data=request.data)
        
        
        # to_return = {}
        # if serializer.is_valid():
        #     data = serializer.save()
        #     return Response({
        #     "data": CustomerSerializer(data, context=self.get_serializer_context()).data,
        #     "status": "success"
        #     })
        # else:
        #     vva = serializer.errors
        #     to_return['data'] = vva
        #     # print(vva['name'].ErrorDetail[0])
        #     to_return['status'] = "Error"

            
        #     return Response(to_return)


        
    

class UpdateForCustomer(generics.UpdateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    def get(self,request,*args,**kwargs):
        try:
            queryset = Customer.objects.get(pk=kwargs['pk'])
            serializer = CustomerSerializer(queryset)
            
            
            return Response({"data":serializer.data,"status":"success"})
        except Snippet.DoesNotExist:
            return Response({"status":"error"},status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        

        serializer = CustomerSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"data":serializer.data,"status":"success"})
        else:
            errorr = serializer.errors
            errorr['status'] = "Error"

            return Response(errorr)
        

        

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"status":"success","message":"deleted Successfully","status":"success"})
    





class SortForCustomer(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['date_time_created','date_created', 'name','address','city','location','pincode','state','country','district','gst_number','gst_type','email','phone']
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'
    
    
    ordering_fields = ['date_time_created','date_created', 'name','address','city','location','pincode','state','country','district','gst_number','gst_type','email','phone']

class PartialSearchForCustomer(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    
    search_fields = ['name']
    
    
    
        

    