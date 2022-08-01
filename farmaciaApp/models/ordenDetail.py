#from tkinter import CASCADE 
#from django.db import models
#from .bill import Bill
#from .product import Product

#class OrdenDetail (models.Model):
#    id = models.BigAutoField(primary_key=True)
#    orden = models.ForeignKey(Bill, related_name='ordenDetail', on_delete=CASCADE)
#    product = models.ForeignKey(Product, related_name='ordenDetail', on_delete=CASCADE)
#    price = models.FloatField('Price', max_length=100)
#    amount = models.IntegerField('Amount', max_length=100)