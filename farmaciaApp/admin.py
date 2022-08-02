from django.contrib import admin
from .models.user import User
from .models.bill import Bill
from .models.ordenDetail import OrdenDetail
from .models.product import Product

admin.site.register(User)
admin.site.register(Bill)
admin.site.register(OrdenDetail)
admin.site.register(Product)

# Register your models here.
