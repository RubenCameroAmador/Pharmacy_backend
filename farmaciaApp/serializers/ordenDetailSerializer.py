from itertools import product
from farmaciaApp.models.ordenDetail import OrdenDetail
# from farmaciaApp.models.bill import Bill
# from farmaciaApp.models.product import Product
from rest_framework import serializers

class OrdenDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenDetail
        fields = ['price','amount']