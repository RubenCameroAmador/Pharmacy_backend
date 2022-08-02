from farmaciaApp.models.product import Product
# from farmaciaApp.models.ordenDetail import OrdenDetail
# from farmaciaApp.serializers.ordenDetailSerializer import OrdenDetailSerializer
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    # ordenDetail = OrdenDetailSerializer()
    class Meta:
        model= Product,
        fields= ['name','description','unit_price','expiration_date','amount','cooled','image_link','category']  #quito orden detail

    def to_representation(self, obj):
        product = Product.objects.get(id= obj.id)
        # ordenDetail = OrdenDetail.objects.get(product = obj.id)
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
            # 'ordenDetail': {
            #     'id': ordenDetail.id,
            #     'bill': ordenDetail.bill,     #esto no lo tengo claro. El bill es otra FK  PUEDE FALLAR
            #     'price': ordenDetail.price,
            #     'amount': ordenDetail.amount,
            # }
        }
    
    def create(self, validated_data):
        # ordenDetailData = validated_data.pop('ordenDetail')
        productInstance = Product.objects.create(**validated_data)
        # OrdenDetail.objects.create(product = productInstance,**ordenDetailData)
        return productInstance

