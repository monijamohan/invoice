from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import invoice, items
from .forms import InvoiceForm, ItemsForm

def index(request):

    
    newbill = nextbill()+1
    invoices = newbill-1
    invoicetable = invoice.objects.all()
    itemstable = items.objects.all()
    context = {
        'invoicetable':invoicetable,
        'itemstable':itemstable,
        'newbill':newbill,
        'invoices':invoices,
    }

    if request.method == 'POST':
        skip_or_proceed = request.POST.get("hidden_data")
        print(skip_or_proceed)
        tax_percent         = request.POST.get("tax")
        discount_percent    = request.POST.get("discount")
        sub_total           = request.POST.get("subtotal1")
        tax_amount          = request.POST.get("taxamount1")
        discount_amount     = request.POST.get("discountamount1")
        grand_total         = request.POST.get("grandtotal1")
        item_no = request.POST.get("item_no")
        j = int(item_no)
        item = ["a"]*j
        quantity = ["a"]*j
        price = ["a"]*j
        for i in range(j):
            item[i]=request.POST.get("item"+str(i+1))
            quantity[i]=request.POST.get("quantity"+str(i+1))
            price[i]=request.POST.get("price"+str(i+1))

        for i in range(j):
            ItemsForm = items.objects.create(invoice_no = newbill, item_no=i, item=item[i], quantity=quantity[i], price=price[i])

        if skip_or_proceed =="skip":
            name    = "unknown"
            phone   = "unknown"
            address = "unknown"
            email   = "unknown"
            pincode = "0"
        elif skip_or_proceed == "proceed":
            name    = request.POST.get("name-field")
            phone   = request.POST.get("phone-field")
            address = request.POST.get("address-field")
            email   = request.POST.get("email-field")
            pincode = request.POST.get("pin-field")
        InvoiceForm = invoice.objects.create(name=name,address=address,phone=phone,email=email,pincode=pincode,invoice_no=newbill,tax_percent=tax_percent,discount_percent=discount_percent,sub_total=sub_total,tax_amount=tax_amount,discount_amount=discount_amount,grand_total=grand_total )
    return render(request, 'blog/index.html', context)

def nextbill():
    lastrecord = invoice.objects.all().last()
    if not lastrecord:
        return 0
    else:
        return int(lastrecord.invoice_no)
