from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager (BaseUserManager):
    def create_user(self,username,password = None):
        if not username:
            raise ValueError('Usuario ya existente')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,password = None):
        user = self.create_user(username = username,password=password,)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username',max_length=30,unique=True)
    password = models.CharField('Password',max_length=256)
    name = models.CharField('Name',max_length=100)
    lastname = models.CharField('Lastname',max_length=100)
    address = models.CharField('Address',max_length=100)
    city = models.CharField("City", max_length=50)
    email = models.EmailField ('Email',max_length=256)
    phone_number = models.CharField('Phone_number',max_length=15)

    def save(self, **kwargs):
        some_salt =  'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'