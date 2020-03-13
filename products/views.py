from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request): #This basically Deep passes a refrence that HTTP has requested.
    product =Product.objects.all()
    return render(request,"index.html", #No need to import temlate django automatically looks for template directory and we just have to pass the template name to it.
                  {"product":product}) #This is a dictionary used as context where a object is passed with a new variable name.


def new(a): #The variable passed to this function can be any but it takes in request addres
    return HttpResponse(" New product available!!")