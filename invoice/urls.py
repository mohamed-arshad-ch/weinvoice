from django.urls import path
from .views import *
urlpatterns = [
    path('api/v1/inventory/create',CreateInventory.as_view(),name="createinventory")
    
]