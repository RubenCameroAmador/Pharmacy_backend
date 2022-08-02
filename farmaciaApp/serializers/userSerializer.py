from farmaciaApp.models.user import User
from farmaciaApp.models.bill import Bill
from farmaciaApp.serializers.billSerializer import BillSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    bill= BillSerializer()
    class Meta:
        model = User
        fields = ['id','username','password','name','lastname','address','city','email','phone_number','bill']
    
    def to_representation(self, obj):
        user = User.objects.get(id = obj.id) 
        bill = Bill.objects.get(user= obj.id)
        return {
            'id':user.id,
            'username':user.username,
            'name': user.name,
            'lastname': user.lastname,
            'email':user.email,
            'address': user.address,
            'city': user.city,
            'email': user.email,
            'phone_number': user.phone_number,
            'bill': {
                'id':bill.id,
                'transaction_date': bill.transaction_date,
                'total_price':bill.total_price,
                'state_orden': bill.state_orden,
            }
        }
    
    def create(self, validated_data):
        billData = validated_data.pop('bill')
        userInstance = User.objects.create(**validated_data)
        Bill.objects.create(user = userInstance,**billData)
        return userInstance