from itertools import product
from farmaciaApp.models.ordenDetail import OrdenDetail
# from farmaciaApp.models.bill import Bill
# from farmaciaApp.models.product import Product
from rest_framework import serializers

class OrdenDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenDetail
        fields = ['price','amount']
    

    # def to_representation(self, obj):
    #     ordenDetail = OrdenDetail.objects.get(id = obj.id)  #revisar con el profe
    #     product = product.objects.get(id = obj.id)          #revisar con el profe
    #     bill = Bill.objects.get(user= obj.id)               #revisar con el profe
    #     return {
    #         'id':ordenDetail.id,
    #         'price': ordenDetail.price,
    #         'amount': ordenDetail.amount,
    #         'bill': {
    #             'id':bill.id,
    #             'transaction_date': bill.transaction_date,
    #             'total_price':bill.total_price,
    #             'state_orden': bill.state_orden,
    #         },
    #         'product':{
    #             'id':product.id,
    #             'name':product.name,
    #             'description': product.description,
    #             'unit_price': product.unit_price,
    #             'expiration_date': product.expiration_date,
    #             'amount': product.amount,
    #             'cooled': product.cooled,
    #             'image_link': product.image_link,
    #             'category': product.category,
    #         },
    #     }
    
    # def create(self, validated_data):
    #     billData = validated_data.pop('bill')
    #     productData = validated_data.pop('product')
    #     ordenDetailInstance = OrdenDetail.objects.create(**validated_data)
    #     Bill.objects.create(user = ordenDetailInstance,**billData)  #REVISARLO CON EL PROFE 
    #     Product.objects.create(**productData)                       #REVISARLO CON EL PROFE
    #     return ordenDetailInstance
    
    