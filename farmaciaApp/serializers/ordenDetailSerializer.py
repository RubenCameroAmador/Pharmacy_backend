from itertools import product
from farmaciaApp.models.ordenDetail import OrdenDetail
from farmaciaApp.models.bill import Bill
from farmaciaApp.models.product import Product
from rest_framework import serializers

class OrdenDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenDetail
        fields = ['price','amount']#,'product']

    # def to_representation(self, obj):
    #     bill = Bill.objects.get(id = obj.id)
    #     product = Product.objects.get(id = id) # verificar esto porque como necesito es una lista de productos creo?
    #     print(product)
    #     return {}

    # def create(self, validated_data):

    #     ordenDetailInstance = OrdenDetail.objects.create(**validated_data)
    #     ## No debo crear un usario, debo crear es los registros de la orden

    #     return ordenDetailInstance