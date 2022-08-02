from farmaciaApp.models.bill import Bill
from farmaciaApp.models.ordenDetail import OrdenDetail
from farmaciaApp.serializers.ordenDetailSerializer import OrdenDetailSerializer
from rest_framework import serializers

class BillSerializer( serializers.ModelSerializer):
    ordenDetail = OrdenDetailSerializer()
    class Meta:
        model = Bill
        fields = ['transaction_date', 'total_price','state_orden','ordenDetail'] #agregué el campo ordenDetail

    def to_representation(self, obj):
        bill = Bill.objects.get(id= obj.id)
        ordenDetail = OrdenDetail.objects.get(bill = obj.id) 
        return {
            'id':bill.id,
            'transaction_date': bill.transaction_date,
            'total_price':bill.total_price,
            'state_orden': bill.state_orden,
            'ordenDetail': {
                'id': ordenDetail.id,
                'product': ordenDetail.product,     #esto no lo tengo claro. El product es otra FK PUEDE FALLAR
                'price': ordenDetail.price,
                'amount': ordenDetail.amount,
            }
        }

    def create(self, validated_data):
        ordenDetailData = validated_data.pop('ordenDetail')
        billInstance = Bill.objects.create(**validated_data)
        OrdenDetail.objects.create(bill = billInstance,**ordenDetailData)
        return billInstance