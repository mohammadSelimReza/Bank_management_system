from django.db import models
from .constants import ACCOUNT_TYPE,GENDER_TYPE
from django.contrib.auth.models import User

# Create your models here.
class UserRegistration(models.Model):
    user = models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10,choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=10,choices=GENDER_TYPE)
    initial_deposit_date = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(default=0,max_digits=12,decimal_places=2)
    
    def __str__(self) -> str:
        return self.user.username
    
class UserAddress(models.Model):
    user = models.OneToOneField(User,related_name='address',on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postal_code = models.IntegerField(max_length=20)
    country = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.user.username
    