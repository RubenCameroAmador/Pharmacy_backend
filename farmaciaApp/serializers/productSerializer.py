from dataclasses import fields
from farmaciaApp.models.product import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product,
        fields= ['name','description','unit_price','expiration_date','amount','cooled','image_link','category']
