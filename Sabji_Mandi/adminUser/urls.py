
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.home,name="homeAdmin"),
    path('customer/',views.customer_tbl),
    path('product/', views.product_tbl),
    path('order/',views.order_tbl),
    path('productform/', views.product_tbl),
    path('addproduct/', views.add_product, name="addproduct"),
    path('delete/<product_id>', views.delete_product, name="deleteproduct"),
    path('edit/<product_id>', views.edit_product, name="editproduct"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)