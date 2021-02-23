from django.urls import path
from .views import *
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


    path('api/v1/compony/create',CreateForCompony.as_view(),name="createinvoice"),
    path('api/v1/compony/update/<str:pk>',UpdateForCompony.as_view(),name="updatecustomer"),
    path('api/v1/compony/read/<str:pk>',UpdateForCompony.as_view(),name="updatecustomer"),
    path('api/v1/compony/delete/<str:pk>',UpdateForCompony.as_view(),name="deleteinventory"),




    
]