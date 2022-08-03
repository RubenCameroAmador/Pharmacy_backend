from farmaciaApp.models.product import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= ['name','description','unit_price','expiration_date','amount','cooled','image_link','category']  #quito orden detail

    def to_representation(self, obj):
        product = Product.objects.get(id= obj.id)
        return {
            'id':product.id,
            'name': product.name,
            'description':product.description,
            'unit_price': product.unit_price,
            'expiration_date': product.expiration_date,
            'amount': product.amount,
            'cooled': product.cooled,
            'image_link': product.image_link,
            'category': product.category,
        }
    
    def create(self, validated_data):
        productInstance = Product.objects.create(**validated_data)
        return productInstance

