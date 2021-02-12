from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import *
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

