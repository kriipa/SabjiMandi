from distutils.command.upload import upload
import email
from django.db import models

# Create your models here.


class customer(models.Model):
    customer_id = models.AutoField(auto_created=True,primary_key=True)
    customer_fname = models.CharField(max_length=25)
    customer_lname = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    customer_picture = models.FileField(upload_to='profile_pic', default='img1')

    class Meta:
        db_table = 'customer_table'
