from audioop import reverse
from http import client
from pydoc import resolve
from django.test import TestCase, SimpleTestCase
from django.urls import path

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_index_url(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func,)



class TestViews(TestCase):
    def test_case_register_view(self):
        client=client()
        print(client)