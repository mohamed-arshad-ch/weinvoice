from django.urls import path
from .views import *
from knox import views as knox_views
urlpatterns = [
    path('api/v1/inventory/create',CreateInventory.as_view(),name="createinventory"),
    path('api/v1/inventory/update/<str:pk>',UpdateInventory.as_view(),name="updateinventory"),
    path('api/v1/inventory/delete/<str:pk>',UpdateInventory.as_view(),name="deleteinventory"),
    path('api/v1/inventory/search',PartialSearch.as_view(),name="searchinventory"),
    path('api/v1/inventory/all',SortInventory.as_view(),name="sortinventory"),
    

    path('api/v1/customer/create',CreateForCustomer.as_view(),name="createcustomer"),
    path('api/v1/customer/update/<str:pk>',UpdateForCustomer.as_view(),name="updatecustomer"),
    path('api/v1/customer/read/<str:pk>',UpdateForCustomer.as_view(),name="updatecustomer"),
    path('api/v1/customer/delete/<str:pk>',UpdateForCustomer.as_view(),name="deleteinventory"),
    path('api/v1/customer/search',PartialSearchForCustomer.as_view(),name="searchinventory"),
    path('api/v1/customer/all',SortForCustomer.as_view(),name="sortcustomer"),


    path('api/v1/invoice/create',CreateForInvoice.as_view(),name="createinvoice"),
    path('api/v1/invoice/update/<str:pk>',UpdateForInvoice.as_view(),name="updatecustomer"),
    path('api/v1/invoice/read/<str:pk>',ReadOfInvoice.as_view(),name="updatecustomer"),
    path('api/v1/invoice/delete/<str:pk>',UpdateForInvoice.as_view(),name="deleteinventory"),
    path('api/v1/invoice/search',PartialSearchForInvoice.as_view(),name="searchinventory"),
    path('api/v1/invoice/all',SortForInvoice.as_view(),name="sortcustomer"),


    path('api/v1/company/create',CreateForCompony.as_view(),name="createinvoice"),
    path('api/v1/company/update/<str:pk>',UpdateForCompony.as_view(),name="updatecustomer"),
    path('api/v1/company/read/<str:pk>',UpdateForCompony.as_view(),name="updatecustomer"),
    path('api/v1/company/all',SortForCompany.as_view(),name="sortcustomer"),
    path('api/v1/company/delete/<str:pk>',UpdateForCompony.as_view(),name="deleteinventory"),

    path('api/v1/excel/create',ExcelConvert.as_view(),name="deleteinventory"),


    path('api/v1/tax/create',CreateForTax.as_view(),name="createinvoice"),
    path('api/v1/tax/update/<str:pk>',UpdateForTax.as_view(),name="updatecustomer"),
    path('api/v1/tax/read/<str:pk>',UpdateForTax.as_view(),name="updatecustomer"),
    path('api/v1/tax/delete/<str:pk>',UpdateForTax.as_view(),name="deleteinventory"),
    path('api/v1/tax/all',SortForTax.as_view(),name="sortcustomer"),
    path('api/v1/tax/search',PartialSearchForTax.as_view(),name="searchinventory"),

    path('api/v1/user/create',RegisterAPI.as_view(),name="createinvoice"),
    path('api/v1/user/update/<str:pk>',UpdateForUser.as_view(),name="updatecustomer"),
    path('api/v1/user/read/<str:pk>',UpdateForUser.as_view(),name="updatecustomer"),
    path('api/v1/user/delete/<str:pk>',UpdateForUser.as_view(),name="deleteinventory"),
    path('api/v1/user/all',SortForUser.as_view(),name="sortcustomer"),
    path('api/v1/user/login/', LoginAPI.as_view(), name='login'),
    path('api/v1/user/is_login', SortForToken.as_view(), name='login'),
    path('api/v1/user/read', ReadForToken.as_view(), name='login'),

    path('api/logout/', GeneratePDF.as_view(), name='logout'),



    
]