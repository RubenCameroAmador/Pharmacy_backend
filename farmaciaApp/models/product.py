from django.db import models

class Product (models.Model):
    id = models.BigAutoField(primary_key= True)
    name = models.CharField('Name', max_length=100)
    description = models.CharField('Description', max_length=500)
    unit_price = models.FloatField('Unit_price', max_length=100)
    expiration_date = models.DateField('Expiration_date')
    amount = models.IntegerField('Amount', max_length=100)
    cooled = models.BooleanField('Cooled', default=False)
    image_link = models.CharField('Image_link', max_length=500)
    category = models.CharField('Category', max_length=100, default="medicamentos")
    #CATEGORY = (
    #    ('belleza', "Belleza"),
    #    ('higiene_personal', 'Higiene personal'),
    #    ('dermocosmetica', 'Dermocosmetica'),
    #    ('cuidado_capilar', 'Cuidado capilar'),
    #    ('infantil','Infantil'),
    #    ('medicamentos', 'Medicamentos'),
    #)