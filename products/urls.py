from django.urls import path,include
from . import views #Use this to import the views module from current directory.

urlpatterns=[
    path("",views.index),
    path("new/",views.new)
]