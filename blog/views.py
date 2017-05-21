from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from blog.forms import CustomerForm , ProductForm
from blog.models import Product



def index(request):
 productform = ProductForm(request.POST, prefix='product')
 customerform = CustomerForm(request.POST, prefix='customer')
 
 if request.method == 'POST':
        full_name = request.POST.get('fullname')
        phone_number = request.POST.get('phonenumber')
        adress = request.POST.get('adress')
        email_ID = reuest.POST.get('emailid')
        pincode = request.POST.get('pincode')
        customerform = Customer.objects.create(full_name=fullname, phone_number=phonenumber, adress=adress , email_ID=emailid, pincode=pincode)
    
    
 else:
      customerform = CustomerForm(prefix='customer')
     
 return render(request, 'blog/index.html' ,{'customerform':customerform})
