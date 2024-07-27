from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE,GENDER_TYPE
from .models import UserAddress,UserRegistration
class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.CharField(max_length=10,choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    postal_code = forms.CharField(max_length=20)
    country = forms.CharField(max_length=50)
    
    class Meta:
        model: User
        fields = ['username','first_name','last_name','email','password1','password2','account_type','gender','birth_date','street_address','city','postal_code','country']
        
    def save(self,commit=True):
        user = super().save(commit=False)
        if commit == True:
            user.save()
            account_type = self.cleaned_data.get('account_type')
            gender = self.cleaned_data.get('gender')
            birth_date = self.cleaned_data.get('birth_date')
            street_address = self.cleaned_data.get('street_address')
            postal_code = self.cleaned_data.get('postal_code')
            city = self.cleaned_data.get('city')
            country = self.cleaned_data.get('country')
            
            UserAddress.objects.create(
                user = user,
                street_address = street_address,
                postal_code = postal_code,
                city = city,
                country = country,
            )
            
            UserRegistration.objects.create(
                user = user,
                account_type = account_type,
                gender = gender,
                birth_date = birth_date,
                account_no = 202419990000 + user.id
            )
        return user
            