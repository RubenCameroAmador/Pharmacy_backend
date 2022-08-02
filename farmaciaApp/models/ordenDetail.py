from django.db import models
from .bill import Bill
from .product import Product

class OrdenDetail (models.Model):
    id = models.BigAutoField(primary_key=True)
    bill = models.ForeignKey(Bill, related_name='ordenDetail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='ordenDetail', on_delete=models.CASCADE)
    price = models.FloatField('Price', max_length=100)
    amount = models.IntegerField('Amount', max_length=100)