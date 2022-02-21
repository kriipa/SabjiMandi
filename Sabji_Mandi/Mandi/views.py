
from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator
from authenticate import *
from Mandi.forms import *

# Create your views here.


@Authentication.valid_customer
def homepage(request):
    veg = Products.objects.filter(product_desc='vegetables')
    fruit = Products.objects.filter(product_desc='fruits')
    spices = Products.objects.filter(product_desc='spices')
    username = request.session['username']
    user = Customer.objects.get(username=username)

    if request.method == "POST":
        contact = Contact_form(request.POST)
        if contact.is_valid():
            contact.save()
            return redirect("/")

    return render(request, 'homepage.html', {'user': user, 'veg': veg, 'fruit': fruit, 'spices': spices})


def register(request):
    if request.method == "POST":
        form = Customer_form(request.POST)
        username = request.POST['username']
        if form.is_valid():
            if Customer.objects.filter(username=username).exists():
                messages.error("Username already exists")
                return redirect("/register/")
            else:
                form.save()
                return redirect("/login/")

    return render(request, 'registration/regis.html')


def login(request):
    if request.method == "POST":
        request.session.clear()
        username = request.session['username'] = request.POST['username']
        password = request.session['password'] = request.POST['password']
        user = Customer.objects.get(username=username, password=password)
        if user is not None:
            Customer.objects.filter(username=username).update(is_login=True)
            return redirect("/home/")
        else:
            return redirect("/login")
    return render(request, 'login/login.html')


def contact(request):
    username = request.session['username']
    user = Customer.objects.get(username=username)

    if request.method == "POST":
        contact = Contact_form(request.POST)
        if contact.is_valid():
            if user.is_login == True:
                contact.save()
                messages.success(request, 'Sent Successfully! Stay in touch')
                return redirect("/contact/")
            else:
                contact.save()
                messages.success(request, 'Sent Successfully! Stay in touch')
                return redirect("/")

    return render(request, 'contact/contact.html', {'user': user})


def viewcart(request):
    return render(request, 'viewCart/viewcart.html')


def about(request):
    return render(request, 'about/about.html')


def logout(request):
    username = request.session['username']
    Customer.objects.filter(username=username).update(is_login=False)
    request.session.clear()
    return redirect("/")

# @Authentication.valid_customer


def home(request):
    veg = Products.objects.filter(product_desc='vegetables')
    fruit = Products.objects.filter(product_desc='fruits')
    spices = Products.objects.filter(product_desc='spices')

    if request.method == "POST":
        contact = Contact_form(request.POST)
        if contact.is_valid():
            contact.save()
            return redirect("/")

    return render(request, 'homepage.html',  {'veg': veg, 'fruit': fruit, 'spices': spices})


@Authentication.valid_customer_where_id
def update(request, customer_id):
    user = Customer.objects.get(customer_id=customer_id)
    if request.method == "POST":
        forms = Customer_form(request.POST, request.FILES, instance=user)
        forms.save()
        return redirect("/login/")

    return render(request, 'update/update_profile.html', {'user': user})


@Authentication.valid_customer
def allproduct(request):
    username = request.session['username']
    user = Customer.objects.get(username=username)
    product = Products.objects.all()
    paginator = Paginator(product, 8)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    return render(request, 'product/allproduct.html', {'products': paged_product, 'user': user})


def order(request, p_id):
    product = Products.objects.get(product_id=p_id)
    if request.method == 'POST':
        form = Order_form(request.POST, request.FILES)
        print(request)
        if form.is_valid():
            form.save()
            messages.success(request, "Order Place Sucessfully.")

            form = Order_form()
    return render(request, "buypage/buypage.html", {'product': product})


def buyfinal(request):
    if request.method == "POST":
        
        form = Order_form(request.POST)
        print(form)
        if form.is_valid():

            form.save()
            return redirect("/")
    else:
        form = Order_form()
    return render(request, 'buypage/buypage.html', {'form': form,})


