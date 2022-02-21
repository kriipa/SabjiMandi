from django.shortcuts import redirect, render
from Mandi.models import *
from Mandi.forms import *
from .models import *
from .form import *
from django.contrib import messages
from authenticate import *
from .models import *
from django.core.paginator import Paginator


# Create your views here.


@Authentication.valid_admin
def home(request):
    username = request.session['username']
    total_user = Customer.objects.all().count
    total_product = Products.objects.all().count
    total_order = Order.objects.all().count

    user = AdminDb.objects.get(username=username)
    return render(request, 'admin/index.html', {"user": user, 'totaluser': total_user, 'totalproduct': total_product, 'totalorder': total_order})


@Authentication.valid_admin
def customer_tbl(request):
    customer = Customer.objects.all()
    return render(request, 'admin/customer.html', {'user': customer})


@Authentication.valid_admin
def product_tbl(request):
    product = Products.objects.all()
    return render(request, 'admin/product.html', {'product': product})


# @Authentication.valid_admin
def order_tbl(request):
    order = Order.objects.raw("select * from order_tbl")
    paginator1 = Paginator(order, 5)
    orderpage = request.GET.get('page')
    paged_order = paginator1.get_page(orderpage)
    return render(request, "admin/order.html", {'order': paged_order})


@Authentication.valid_admin
def add_product(request):
    # product = Products.objects.all()
    if request.method == "POST":
        form = Product_form(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("/admin/product/")
        else:
            return redirect("/admin/addproduct/")
    return render(request, 'admin/productform.html')


@Authentication.valid_admin_where_id
def delete_product(request, p_id):
    product = Products.objects.get(product_id=p_id)
    product.delete()

    return redirect("/admin/product/")


@Authentication.valid_admin_where_id
def edit_product(request, p_id):
    product = Products.objects.get(product_id=p_id)
    if request.method == "POST":
        forms = Product_form(request.POST, request.FILES, instance=product)
        forms.save()
        messages.success(request, "Product Updated Successfully")
        return redirect("/admin/product/")

    return render(request, 'admin/edit.html', {'product': product})


def login(request):
    if request.method == "POST":
        username = request.session['username'] = request.POST['username']
        request.session['password'] = request.POST['password']
        AdminDb.objects.filter(username=username).update(is_admin=True)
        return redirect('/admin/index/')

    return render(request, 'admin/login.html')


def register(request):
    if request.method == "POST":
        form = AdminDbForm(request.POST)
        email = request.POST['email']
        username = request.POST['username']
        if form.is_valid():
            if AdminDb.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('/admin/adminregister/')
            elif AdminDb.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('/admin/register/')
            else:
                form.save()
                print(form)
                return redirect("/admin/index/")

    return render(request, 'admin/registration.html')


def logout(request):
    request.session.flush()
    return redirect("/admin/login/")


def mywebsite(request):
    request.session.clear()
    return redirect("/")


@Authentication.valid_admin
def addcustomer(request):
    if request.method == "POST":
        form = Customer_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "User Added Successful")
            return redirect("/admin/customer/")
    return render(request, 'admin/addcustomer.html')


def delete(request, order_id):
    order = Order.objects.filter(order_id=order_id)
    order.delete()
    return redirect("/admin/order/")
