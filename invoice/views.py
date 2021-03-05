from django.shortcuts import render
from rest_framework import generics, permissions,viewsets
from rest_framework.response import Response
from .serializers import *
import  os
from django.core.files.storage import FileSystemStorage
import pandas
from django.db.models import Case, CharField, Value, When
from django.core.paginator import Paginator

from rest_framework import filters
from webinvoice import settings as newsetting
from datetime import date

from django.core.files import File
from io import BytesIO

from django.conf import settings as django_settings
from django.template.loader import get_template
from django.http import HttpResponse
from django.views.generic import View
from invoice.utils import render_to_pdf
from knox.models import AuthToken
from knox.models import AuthToken
from django.contrib.auth import authenticate
from .sortconroll import *
from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from  rest_framework.mixins import CreateModelMixin
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from datetime import date
from knox.views import LoginView as KnoxLoginView
# from pandas import *
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
    filterset_fields = ['date_created','name','hsn','base_price','sales_price','stock','unit','cgst','sgst','cess','others','barcode']
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'
    
    
    ordering_fields = ['date_created','name','hsn','base_price','sales_price','stock','unit','cgst','sgst','cess','others','barcode']

class PartialSearch(generics.ListAPIView):
    
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'
    

    def get(self,request):
        
        name = request.GET.get('name')

        instance = Inventory.objects.filter(name__icontains=name)
        
        print(instance)
        if instance.exists():
            
            serializer = InventorySerializer(instance,many=True)
            return Response({"data":serializer.data,"status":"success"})
        else:
            return Response({"data":"error","status":"error"})


class CreateForCustomer(CreateModelMixin,generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        
        
        to_return = {}
        if serializer.is_valid():
            data = serializer.save()
            return Response({
            "data": CustomerSerializer(data, context=self.get_serializer_context()).data,
            "status": "success"
            })
        else:
            vva = serializer.errors
            to_return['data'] = vva
            # print(vva['name'].ErrorDetail[0])
            to_return['status'] = "Error"

            
            return Response(to_return)


        
    

class UpdateForCustomer(generics.UpdateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    def get(self,request,*args,**kwargs):
        try:
            queryset = Customer.objects.get(pk=kwargs['pk'])
            serializer = CustomerSerializer(queryset)
            
            
            return Response({"data":serializer.data,"status":"success"})
        except Customer.DoesNotExist:
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
    
    
    
        

class CreateForInvoice(generics.CreateAPIView):
    queryset =Invoice.objects.all()
    serializer_class = InvoiceWriteSerializer
    
    def post(self, request, *args, **kwargs):
        
        to_return = {}
        controller = CreateInvoiceController(data=request.data)
        createddata = controller.create()
        
        movies_serializer = InvoiceReadSerializer(createddata)
        to_return['data'] = movies_serializer.data

        to_return['status'] = "Success"
        
        pdfs = generate_obj_pdf(movies_serializer.data['id'],request)
        to_return['pdf_url'] = pdfs
        return Response(to_return)
       







       

class ReadOfInvoice(APIView):
    



    def get(self,request,*args,**kwargs):
        try:
            to_return = {}
            invoice = Invoice.objects.get(pk=kwargs['pk'])
            movies_serializer = InvoiceReadSerializer(invoice)
            to_return['data'] = movies_serializer.data
            to_return['status'] = "Success"
            HOSTNAME = request.META['HTTP_HOST']
            url = '{0}/static/img/{1}'.format(HOSTNAME,invoice.pdf)
            to_return['pdf_url'] = url
            return Response(to_return)
        except Invoice.DoesNotExist:
            return Response({"data":"No Data Availabel","status":"Error"})


class UpdateForInvoice(generics.UpdateAPIView):
    serializer_class = InvoiceWriteSerializer
    queryset = Invoice.objects.all()
    def get(self,request,*args,**kwargs):
        try:
            queryset = Invoice.objects.get(pk=kwargs['pk'])
            serializer = InvoiceReadSerializer(queryset)
            HOSTNAME = request.META['HTTP_HOST']
            url = '{0}/static/img/{1}'.format(HOSTNAME,queryset.pdf)
            
            
            return Response({"data":serializer.data,"status":"success","pdf_url":url})
        except Invoice.DoesNotExist:
            return Response({"data":"Invoice Not Exist","status":"error"},status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        pdfs = generate_obj_pdf(instance.id,request)
        
        serializer = InvoiceWriteSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"data":InvoiceReadSerializer(data, context=self.get_serializer_context()).data,"status":"success","pdf_url":pdfs})
        else:
            errorr = serializer.errors
            errorr['status'] = "Error"

            return Response(errorr)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"status":"success","message":"deleted Successfully","status":"success"})


class SortForInvoice(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceReadSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['date_created','customer__name','company_name','company_address','company_city','company_location','company_pin','company_district','company_state','company_gstin','company_email','company_phone','company_logo','product_list','due_amount','sgst','cgst','status','invoice_type']
    # pagination_class = PageNumberPagination
    # pagination_class.page_size_query_param = 'limit'
    
    
    ordering_fields = "__all__"

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"data":serializer.data})

class PartialSearchForInvoice(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceReadSerializer
    
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    
    search_fields = ['customer__name']



class CreateForCustomer(CreateModelMixin,generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        
        
        to_return = {}
        if serializer.is_valid():
            data = serializer.save()
            return Response({
            "data": CustomerSerializer(data, context=self.get_serializer_context()).data,
            "status": "success"
            })
        else:
            vva = serializer.errors
            to_return['data'] = vva
            # print(vva['name'].ErrorDetail[0])
            to_return['status'] = "Error"

            
            return Response(to_return)


        
class UpdateForCustomer(generics.UpdateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    def get(self,request,*args,**kwargs):
        try:
            queryset = Customer.objects.get(pk=kwargs['pk'])
            serializer = CustomerSerializer(queryset)
            
            
            return Response({"data":serializer.data,"status":"success"})
        except Snippet.DoesNotExist:
            return Response({"status":"error"},status=status.HTTP_200_OK)

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
    filterset_fields = ['date_time_created','date_created', 'name','address','city','location','pincode','state','country','district','gst_number','gst_type','email','phone','store_id']
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'
    
    
    ordering_fields = ['date_time_created','date_created', 'name','address','city','location','pincode','state','country','district','gst_number','gst_type','email','phone','store_id']

class PartialSearchForCustomer(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    
    search_fields = ['name']
    
    
    
        

class CreateForCompony(generics.CreateAPIView):
    queryset =Compony.objects.all()
    serializer_class = ComponySerializer
    
    def post(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        
        
        to_return = {}
        if serializer.is_valid():
            data = serializer.save()
            return Response({
            "data": ComponySerializer(data, context=self.get_serializer_context()).data,
            "status": "success"
            })
        else:
            vva = serializer.errors
            to_return['data'] = vva
            # print(vva['name'].ErrorDetail[0])
            to_return['status'] = "Error"

            
            return Response(to_return)
       







       




class UpdateForCompony(generics.UpdateAPIView):
    serializer_class = ComponySerializer
    queryset = Compony.objects.all()
    def get(self,request,*args,**kwargs):
        try:
            queryset = Compony.objects.get(pk=kwargs['pk'])
            serializer = ComponySerializer(queryset)
            
            
            return Response({"data":serializer.data,"status":"success"})
        except Compony.DoesNotExist:
            return Response({"data":"Company Not Exist","status":"error"},status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        

        serializer = ComponySerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"data":ComponySerializer(data, context=self.get_serializer_context()).data,"status":"success"})
        else:
            errorr = serializer.errors
            errorr['status'] = "Error"

            return Response(errorr)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"status":"success","message":"deleted Successfully","status":"success"})


class SortForCompany(generics.ListAPIView):
    queryset = Compony.objects.all()
    serializer_class = ComponySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company_id']





class ExcelConvert(generics.CreateAPIView):
    serializer_class = ExcelConvert
    def post(self,request):
        request_file = request.FILES['files'] if 'files' in request.FILES else None
        if request_file: 
             
            fs = FileSystemStorage() 
            file = fs.save(request_file.name, request_file) 
            
            fileurl = fs.url(file) 
            print(fileurl)
        conver_to_pdf = pandas.read_excel('static/img/inventory.xlsx')
        excel_datas = conver_to_pdf.to_dict('records')
    
        for i in range(len(excel_datas)):
            inventory = Inventory.objects.create(name=excel_datas[i]['name'],hsn=excel_datas[i]['hsn'],base_price=excel_datas[i]['base_price'],sales_price=excel_datas[i]['sales_price'],stock=excel_datas[i]['stock'],unit=excel_datas[i]['unit'],cgst=excel_datas[i]['cgst'],sgst=excel_datas[i]['sgst'],cess=excel_datas[i]['cess'],others=excel_datas[i]['others'],barcode=excel_datas[i]['barcode'])
        return Response({"data":excel_datas})

    

class CreateForTax(generics.CreateAPIView):
    queryset =TaxGroup.objects.all()
    serializer_class = TaxSerializer
    
    def post(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        
        
        to_return = {}
        if serializer.is_valid():
            data = serializer.save()
            return Response({
            "data": TaxSerializer(data, context=self.get_serializer_context()).data,
            "status": "success"
            })
        else:
            vva = serializer.errors
            to_return['data'] = vva
            # print(vva['name'].ErrorDetail[0])
            to_return['status'] = "Error"

            
            return Response(to_return)
       







       




class UpdateForTax(generics.UpdateAPIView):
    serializer_class = TaxSerializer
    queryset = TaxGroup.objects.all()
    def get(self,request,*args,**kwargs):
        try:
            queryset = TaxGroup.objects.get(pk=kwargs['pk'])
            serializer = TaxSerializer(queryset)
            
            
            return Response({"data":serializer.data,"status":"success"})
        except TaxGroup.DoesNotExist:
            return Response({"data":"Invoice Not Exist","status":"error"},status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        

        serializer = TaxSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"data":TaxSerializer(data, context=self.get_serializer_context()).data,"status":"success"})
        else:
            errorr = serializer.errors
            errorr['status'] = "Error"

            return Response(errorr)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"status":"success","message":"deleted Successfully","status":"success"})


class SortForTax(generics.ListAPIView):
    queryset = TaxGroup.objects.all()
    serializer_class = TaxSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['date_time_created','date_created', 'hsn_code','hsn_sgst','hsn_cgst','hsn_cess','hsn_others','hsn_user_id']
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'
    
    
    ordering_fields = ['date_time_created','date_created', 'hsn_code','hsn_sgst','hsn_cgst','hsn_cess','hsn_others','hsn_user_id']

class PartialSearchForTax(generics.ListAPIView):
    queryset = TaxGroup.objects.all()
    serializer_class = TaxSerializer
    
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    
    search_fields = ['hsn_code']



class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        
        try:
            usern = CustomUser.objects.get(phone=request.data['phone'])
            
            if usern is not None:
                
                return Response({"data":"User Already Exist","status":"Error"})
            else:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.save()
                return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1],
                "status":"Success"
                })
        except CustomUser.DoesNotExist:

            serializer = self.get_serializer(data=request.data)
            # serializer.is_valid(raise_exception=True)
            if serializer.is_valid():

                user = serializer.save()
                return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1],
                "status":"Success"
                },status=status.HTTP_200_OK)
            else:
                return Response({"data":['Passsword Not Match'],"status":"Error"},status=status.HTTP_200_OK)


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        print(request.data)
        user = authenticate(username=request.data['phone'], password=request.data['password'])
        print(user)
        if user is not None:
            login(request,user)
            newdd = super(LoginAPI, self).post(request, format=None)
            print(newdd.data['token'])
            newdd.data['status'] = "Success"
            newu = CustomUser.objects.get(username=request.data['phone'])
            newu.token = newdd.data['token']
            newu.save()
            return newdd
        else:
            return Response({"data":"Invalid UserName And Password","status":"Error"})
        


class UpdateForUser(generics.UpdateAPIView):
    serializer_class = UserAllSerializer
    queryset = CustomUser.objects.all()
    def get(self,request,*args,**kwargs):
        try:
            queryset = CustomUser.objects.get(pk=kwargs['pk'])
            serializer = UserAllSerializer(queryset)
            
            
            return Response({"data":serializer.data,"status":"success"})
        except CustomUser.DoesNotExist:
            return Response({"data":"Invoice Not Exist","status":"error"},status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        

        serializer = UserAllSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"data":UserAllSerializer(data, context=self.get_serializer_context()).data,"status":"success"})
        else:
            errorr = serializer.errors
            errorr['status'] = "Error"

            return Response(errorr)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"status":"success","message":"deleted Successfully","status":"success"})


class SortForUser(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserAllSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['phone','subscription_plan', 'subscription_start','subscription_end','subscription_status','user_status','unique_id','email','first_name','last_name']
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'
    
    
    ordering_fields = ['phone','subscription_plan', 'subscription_start','subscription_end','subscription_status','user_status','unique_id','email','first_name','last_name']


class SortForToken(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserAllSerializer
    
    def get(self,request):
        token = request.GET.get('token',None)
        
        try:
            userii = CustomUser.objects.get(token=token)
            
            print(userii)
            serializer = UserAllSerializer(userii)

            return Response({"data":True,"status":"success"})
        except CustomUser.DoesNotExist:
            return Response({"data":False,"status":"Error"})


class ReadForToken(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserAllSerializer
    
    def get(self,request):
        token = request.GET.get('token',None)
        
        try:
            userii = CustomUser.objects.get(token=token)
            
            print(userii)
            serializer = UserAllSerializer(userii)

            return Response({"data":serializer.data,"status":"success"})
        except CustomUser.DoesNotExist:
            return Response({"data":"Invalid User","status":"Error"})


def generate_obj_pdf(instance_id,request):
     obj = Invoice.objects.get(id=instance_id)
     context = {'instance': obj}
     pdf = render_to_pdf('invoice.html', context)
     filename = 'Invoice_%s.pdf'%str(obj.id)
     obj.pdf.save(filename, File(BytesIO(pdf.content)))
     print(obj.pdf)
     HOSTNAME = request.META['HTTP_HOST']
     
     url = '{0}/static/img/{1}'.format(HOSTNAME,obj.pdf)

     return url


class InvoiceReportFilter(generics.GenericAPIView):
    queryset= Invoice.objects.all()
    serializer_class= InvoiceReadSerializer
    


    def get(self, request):

        name=request.GET.get("name")
        fromdate=request.GET.get("from")
        todate=request.GET.get("to")
        instance= Invoice.objects.filter(date_created__range=[fromdate, todate], invoice_type=name)


class InvoiceReportFilter(generics.GenericAPIView):
    queryset=Inventory.objects.all()
    serializer_class=InventorySerializer


    def get(self, request):
        name=request.GET.get("name")
        fromdate=request.GET.get("from")
        todate=request.GET.get("to")
        

        instance= Invoice.objects.filter(date_created__range=[fromdate, todate], invoice_type=name)

        total=0
        for i in instance:
            total+=i.due_amount
        print(total)

        if instance.exists():
            serializer= InvoiceReadSerializer(instance, many=True)
            return Response({"data":serializer.data,"sales_price":total,"status":"success"})
        else:
            return Response({"data":"data not available", "status":"error"})



        if instance.exists():
            serializer= InvoiceReadSerializer(instance, many=True)
            return Response({"data":serializer.data,"sales_price":total,"status":"success"})

        else:
            return Response({"data":"data not available", "status":"error"})



class InventoryList(generics.GenericAPIView):
    queryset=Inventory.objects.all()
    serializer_class=InventorySerializer
    def get(self, request):
        fromdate=request.GET.get("from")
        todate=request.GET.get("to")
        inventory=Inventory.objects.filter(date_created__range=[fromdate, todate])
        a=self.paginate_queryset(inventory)
        if inventory.exists():
            serializer=InventorySerializer(a, many=True)
            
            return Response({"data":serializer.data, "status":"success"})
        else:
            return Response({"data":"data not available", "status":"error"})


class InventoryStatusList(generics.GenericAPIView):
    queryset=Inventory.objects.all()
    serializer_class=InventorySerializer
    def get(self,request):

        list_all= Inventory.objects.all().count()

        
        outoff_stock= Inventory.objects.filter(stock__lte=0).count()
        # print(low_stock)
        low_stock=Inventory.objects.filter(stock__lte=3).count()
        list_customer= Customer.objects.all().count()
        sales_invoicecount= Invoice.objects.filter(invoice_type="sales")
        purchase_customer= Invoice.objects.filter(invoice_type="purchase")
        quotation_customer= Invoice.objects.filter(invoice_type="quotation")
        total1=0
        for i in sales_invoicecount:
            total1+=i.due_amount
        total2=0
        for i in purchase_customer:
            total2+=i.due_amount
        total3=0
        for i in quotation_customer:
            total3+=i.due_amount



        return Response({"data":{"inventory_count":list_all,"outoffstock_count":outoff_stock,"low_stock":low_stock,"customer_count":list_customer,"sale_count":total1,"purchase_count":total2,"quotation_count":total3},"status":"success"})

class InventoryLowCountList(generics.GenericAPIView):
    queryset=Inventory.objects.all()
    serializer_class=InventorySerializer
    def get(self,request):
        fromdate=request.GET.get("from")
        todate=request.GET.get("to")
        inventory=Inventory.objects.filter(date_created__range=[fromdate, todate],stock__lte=3)
        p=self.paginate_queryset(inventory)
        if inventory.exists():
            serializer=InventorySerializer(p, many=True)
            
            return Response({"data":serializer.data, "status":"success"})
        else:
            return Response({"data":"data not available", "status":"error"})


class InventoryOutOffCountList(generics.GenericAPIView):
    queryset=Inventory.objects.all()
    serializer_class=InventorySerializer
    def get(self,request):
        fromdate=request.GET.get("from")
        todate=request.GET.get("to")
        inventory=Inventory.objects.filter(date_created__range=[fromdate, todate],stock__lte=0)
        s=self.paginate_queryset(inventory)
        if inventory.exists():
            serializer=InventorySerializer(s, many=True)
            
            return Response({"data":serializer.data, "status":"success"})
        else:
            return Response({"data":"data not available", "status":"error"})

class CreateUnits(CreateModelMixin,generics.GenericAPIView):
    serializer_class=UnitAllSerializer
    def post(self,request, *args, **kwargs):
      
        try:
            units = Units.objects.filter(name__iexact=request.data['name']).count()
            
            if units != 0:
                
                return Response({"data":"Unit Already Exist","status":"Error"},status=status.HTTP_200_OK)
            else:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.save()
                return Response({"data":serializer.data,
                    "status":"Success",
                
                    },status=status.HTTP_200_OK)
        except Units.DoesNotExist:
            serializer = self.get_serializer(data=request.data)
            
           
        
class ListUnitPagination(generics.ListAPIView):
    queryset = Units.objects.all()
    serializer_class = UnitAllSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['name','short_name','status']
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'

class UpdateUnits(generics.UpdateAPIView):
    serializer_class = UnitAllSerializer
    queryset = Units.objects.all()
    def get(self,request,*args,**kwargs):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        

        serializer = UnitAllSerializer(instance, data=request.data, partial=True)
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
    
class PartialSearchForUnits(generics.ListAPIView):
    queryset = Units.objects.all()
    serializer_class = UnitAllSerializer
    
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    
    search_fields = ['name'] 
    

    
        
        
        

               