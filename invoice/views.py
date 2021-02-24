from django.shortcuts import render
from rest_framework import generics, permissions,viewsets
from rest_framework.response import Response
from .serializers import *
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
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from  rest_framework.mixins import CreateModelMixin
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
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
        return Response(to_return)
       







       

class ReadOfInvoice(APIView):
    



    def get(self,request,*args,**kwargs):
        try:
            to_return = {}
            invoice = Invoice.objects.get(pk=kwargs['pk'])
            movies_serializer = InvoiceReadSerializer(invoice)
            to_return['data'] = movies_serializer.data
            to_return['status'] = "Success"
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
            
            
            return Response({"data":serializer.data,"status":"success"})
        except Invoice.DoesNotExist:
            return Response({"data":"Invoice Not Exist","status":"error"},status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        

        serializer = InvoiceWriteSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"data":InvoiceReadSerializer(data, context=self.get_serializer_context()).data,"status":"success"})
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
    filterset_fields = "__all__"
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'
    
    
    ordering_fields = "__all__"

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
    filterset_fields = ['company_id','company_admin']





class ExcelConvert(generics.CreateAPIView):
    serializer_class = ExcelConvert
    def post(self,request):
        pass
        # xls = ExcelFile('static/tests-example.xls')
        # data = xls.parse(xls.sheet_names[0])
        # # print(data.to_dict())
        # full = data.to_dict()

        # for i in full:
            
            
        #     for j in range(len(full[i])):
        #         print(full['id'][j])
    

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
    filterset_fields = ['date_time_created','date_created', 'hsn_code','hsn_sgst','hsn_cgst','hsn_sess','hsn_others','hsn_user_id']
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'limit'
    
    
    ordering_fields = ['date_time_created','date_created', 'hsn_code','hsn_sgst','hsn_cgst','hsn_sess','hsn_others','hsn_user_id']

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
        # try:
        #     user = CustomUser.objects.get(phone=request.data['phone'],password=request.data['password'])
        #     login(request,user)
        #     return super(LoginAPI, self).post(request, format=None)
        # except CustomUser.DoesNotExist:
        #     return Response({"data":"Invalid UserName And Password","Type":"Error"})


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

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = True
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
