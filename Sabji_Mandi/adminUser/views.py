from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'admin/index.html')

def customer_tbl(request):
    return render(request,'admin/customer.html')

def product_tbl(request):
    return render(request,'admin/product.html')


def order_tbl(request):
    return render(request,'admin/order.html')

