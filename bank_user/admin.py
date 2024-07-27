from django.contrib import admin
from .models import UserRegistration,UserAddress
# Register your models here.
admin.site.register(UserAddress)
admin.site.register(UserRegistration)