from farmaciaApp.models.bill import Bill
from rest_framework import serializers

class BillSerializer( serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['transaction_date', 'total_price','state_orden']