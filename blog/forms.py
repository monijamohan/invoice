
from django import forms
from django.forms import ModelForm
from blog.models import Customer, Product  

class CustomerForm(forms.ModelForm):
   adress = forms.CharField( widget=forms.Textarea )
   class Meta:
        model = Customer 
        fields = [ 'full_name' , 'phone_number', 'adress', 'email_ID', 'Pincode' ]


class ProductForm(forms.ModelForm):
   
   class Meta:
        model = Product 
        fields = [ 'item' , 'quantity', 'price' ]


