from farmaciaApp.models.user import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','username','password','name','lastname','address','city','email','phone_number']
    
    def to_representation(self, obj):
        user = User.objects.get(id = obj.id) 
        return {
            'id':user.id,
            'username':user.username,
            'name': user.name,
            'lastname': user.lastname,
            'email':user.email,
            'address': user.address,
            'city': user.city,
            'phone_number': user.phone_number,
        }
    
    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance