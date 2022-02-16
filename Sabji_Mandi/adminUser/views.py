from django.shortcuts import redirect, render
from Mandi.models import *
from Mandi.forms import *

# Create your views here.
def home(request):
    return render(request,'admin/index.html')

def customer_tbl(request):
    return render(request,'admin/customer.html')

def product_tbl(request):
    product = Products.objects.all()
    return render(request,'admin/product.html', {'product':product})

def order_tbl(request):
    return render(request,'admin/order.html')

def add_product(request):
    # product = Products.objects.all()
    if request.method == "POST":
        form = Product_form(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("/admin/product/")
        else :
            return redirect("/admin/addproduct/")
    return render(request, 'admin/productform.html')

def delete_product(request, product_id):
    product = Products.objects.get(product_id = product_id)
    product.delete()

    return redirect("/admin/product/")

def edit_product(request, product_id):
    product = Products.objects.get(product_id = product_id)
    if request.method == "POST":
        forms = Product_form(request.POST, request.FILES, instance=product)
        forms.save()
        return redirect("/admin/product/")
    
    return render(request,'admin/edit.html', {'product':product})
