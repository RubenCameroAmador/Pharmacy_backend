from tkinter import CASCADE
from django.db import models
from .user import User
from .product import Product
#from .ordenDetail import OrdenDetail

class Bill (models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='bill', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)   #manyToMany realtionship #, through=OrdenDetail
    transaction_date = models.DateTimeField()
    total_price = models.FloatField('Total_price', max_length=100)
    state_orden = models.CharField('State_orden',max_length=10)
    #price = models.FloatField('Price', max_length=100)          #lo traje de ordenDetail
    #amount = models.IntegerField('Amount', max_length=100)      #lo traje de ordenDetail
    
