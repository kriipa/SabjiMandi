from audioop import reverse
from http import client
from pydoc import resolve
from django.test import TestCase, SimpleTestCase
from django.urls import path



from django.urls import reverse,resolve



from django.test import SimpleTestCase



from django.test.client import Client

from .views import *






class TestUrls(SimpleTestCase):



    def test_home_url(self):
        url=reverse("homepage")
        self.assertEquals(resolve(url).func,home)



    def test_contact_url(self):
        url=reverse("contact")
        self.assertEquals(resolve(url).func,contact)


    def test_cart_url(self):
        url=reverse("viewcart")
        self.assertEquals(resolve(url).func,viewcart)

    def test_product_url(self):
        url=reverse("allproduct")
        self.assertEquals(resolve(url).func,allproduct)

    def test_buy_url(self):
        url=reverse("buyfinal")
        self.assertEquals(resolve(url).func,buyfinal)
    
    def test_about_url(self):
        url=reverse("about")
        self.assertEquals(resolve(url).func,about)



    