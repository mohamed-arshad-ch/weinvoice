from django.urls import path
from .views import *
urlpatterns = [
    path('api/v1/inventory/create',CreateInventory.as_view(),name="createinventory"),
    path('api/v1/inventory/update/<str:pk>',UpdateInventory.as_view(),name="updateinventory"),
    path('api/v1/inventory/delete/<str:pk>',UpdateInventory.as_view(),name="deleteinventory"),
    path('api/v1/inventory/search',SearchInventory.as_view(),name="searchinventory"),
    path('api/v1/inventory/all',SortInventory.as_view(),name="sortinventory"),

    
]