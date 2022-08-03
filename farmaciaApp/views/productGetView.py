import django
from rest_framework import generics, status
from rest_framework.response import Response


from farmaciaApp.models.product import Product
from farmaciaApp.serializers.productSerializer import ProductSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class ProductGetView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    filter_backends =(DjangoFilterBackend,SearchFilter)
    #filter_fields = ('id','name') # Esta es para filtrar por algun campo
    search_field = ('id','name')

