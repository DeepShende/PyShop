from django.db import models

# Create your models here.They are basically a unit of data that required for repeated uses.It is representation of real world operations such as order,feedback,product..etc.
class Product(models.Model): #The models(module) has a class called Model that has been inherited from class products so that we can use its funtion.
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock =models.IntegerField()
    image_url =models.CharField(max_length=2083) #These are the attributes of this class or model are given type using classes from models module such as CharField and name arguments such as max_length are used when required.

class Offer(models.Model): #There can be classes of models in the module models of an app.
    coupon_code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

# The advantage of django is that it an automatically create tables according to attributes specifies in a class of model
# by using migrations we just need add the app in the settings module of the main directory  and in terminal run python manage.py(intially known as django-admin) makemigrations
# once the migrations are ready just run python manage.py migrate in terminal.